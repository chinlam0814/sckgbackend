from django.http import JsonResponse
from user.models import Admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Texts
import json
from flask import Flask, jsonify, request
from neo4j import GraphDatabase
import openai
import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.graphs.networkx_graph import KG_TRIPLE_DELIMITER
import pprint
from pyvis.network import Network
import networkx as nx
import gradio as gr
from langchain.indexes import GraphIndexCreator
from langchain.chains import graph_qa
from langchain.graphs.networkx_graph import KnowledgeTriple
# Prompt template for knowledge triple extraction
# _DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
#     "You are a networked intelligence helping a human track knowledge triples"
#     " about all relevant people, things, concepts, etc. and integrating"
#     " them with your knowledge stored within your weights"
#     " as well as that stored in a knowledge graph."
#     " Extract all of the knowledge triples from the text."
#     " A knowledge triple is a clause that contains a subject, a predicate,"
#     " and an object. The subject is the entity being described,"
#     " the predicate is the property of the subject that is being"
#     " described, and the object is the value of the property.\n\n"
#     "EXAMPLE\n"
#     "It's a state in the US. It's also the number 1 producer of gold in the US.\n\n"
#     f"Output: (Nevada, is a, state){KG_TRIPLE_DELIMITER}(Nevada, is in, US)"
#     f"{KG_TRIPLE_DELIMITER}(Nevada, is the number 1 producer of, gold)\n"
#     "END OF EXAMPLE\n\n"
#     "EXAMPLE\n"
#     "I'm going to the store.\n\n"
#     "Output: NONE\n"
#     "END OF EXAMPLE\n\n"
#     "EXAMPLE\n"
#     "Oh huh. I know Descartes likes to drive antique scooters and play the mandolin.\n"
#     f"Output: (Descartes, likes to drive, antique scooters){KG_TRIPLE_DELIMITER}(Descartes, plays, mandolin)\n"
#     "END OF EXAMPLE\n\n"
#     "EXAMPLE\n"
#     "{text}"
#     "Output:"
# )

uri = "neo4j://localhost:7687"
user = "neo4j"
password = "Xzq-071797397074"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Create your views here.
def returnJson(data = None, errorCode = 0):
    if data is None:
        data = []
    return JsonResponse({'errorCode' : errorCode, 'data' : data})

def texts_list(request):
    texts = Texts.objects.order_by('-id')
    return returnJson([dict(text.body()) for text in texts])

def text(request, pk):
    if request.method == 'GET':
        text = Texts.objects.get(id=pk)
        return returnJson([dict(text.body())])

@login_required
def create_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        text = Texts.objects.create(text=data['text'], created_by=data['username'], json_created=data['json_created'])
        #text.json_created = generate_json(data['text'])
        #text.json_created = {'text':'abc'}
        text.save()

        return returnJson([dict(text.body())])
        
def delete_text(request, textId):
    if request.method == 'DELETE':
        try:
            text = Texts.objects.get(id=textId)
            text.delete()

            texts = Texts.objects.all()

            return returnJson([dict(text.body()) for text in texts])

        except Texts.DoesNotExists:
            return returnJson([], 400)

def generate_json(text):
    openai.api_key = 'sk-proj-3ulLVu675fEXo9Md8cVXT3BlbkFJkDVUgy73QPQG8Fra3ufR'
    os.environ["http_proxy"] = "http://127.0.0.1:7890"
    os.environ["https_proxy"] = "http://127.0.0.1:7890"

    prompt_template = (
        "你能够找出文本中构建知识图谱的三元组"
        "找出所有相关的人、事、概念"
        "文本包含主语、谓语和宾语"
        "实体1(entity1)为主语"
        "关系(relationship)为谓语"
        "实体2(entity2)为宾语"
        "实体1称为entity1,实体2称为entity2,关系称为relationship"
        "确保返回的是json格式"
        "例子：智慧城市包含智能交通，智慧能源，智慧环境，智慧建筑与住宅，智慧医疗与健康，智慧安防，智慧教育，智慧商业与服务和智慧政府与管理。"
        """输出:  'triples': [{'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智能交通'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧能源'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧环境'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧建筑与住宅'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧医疗与 健康'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧安防'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧教育'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧商业与服务'}, {'entity1': '智慧城市', 'relationship': '包含', 'entity2': '智慧政府与管理'}]"""
    )
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role" : "system",
                "content" : prompt_template,
            },
            {
                "role" : "user",
                "content" : text,
            },
        ],
        max_tokens=4096,
        temperature=0,
    )

    print(response)
    generated_text = response.choices[0].message.content
    print(generated_text)
    
    json_data = json.loads(generated_text)
    print(json_data)

    return (json_data)


# openai.api_key = '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'
#     os.environ["http_proxy"] = "http://127.0.0.1:7890"
#     os.environ["https_proxy"] = "http://127.0.0.1:7890"

# def run_cypher_query(query):
#     with driver.session() as session:
#         result = session.run(query)
#         records = [dict(record) for record in result]
#         return records
        
# def execute_query():
#     # 从请求中获取查询语句
#     query = request.json.get('query', '')

#     return jsonify(query)

    # 执行查询
    # try:
    #     records = run_cypher_query(query)
    #     return jsonify({'success': True, 'data': records})
    # except Exception as e:
    #     return jsonify({'success': False, 'error': str(e)})

# "示例\n"
#         "智慧城市是未来城市发展的重要方向，利用信息技术来提升城市管理效率和市民生活质量。\n\n"
#         f"输出：(智慧城市，是，未来城市发展的重要方向)，（智慧城市，利用，信息技术），（智慧城市，提升，城市管理效率），（智慧城市，提升，市民生活质量）"
#         "示例结束\n"
#         "示例\n"
#         "知识图谱（Knowledge Graph），在图书情报界称为知识域可视化或知识领域映射地图，是显示知识发展进程与结构关系的一系列各种不同的图形，用可视化技术描述知识资源及其载体，挖掘、分析、构建、绘制和显示知识及它们之间的相互联系。"
#         f"输出：无关"
#         "示例结束\n"
#         "示例\n"
#         "模式为知识图谱提供了框架，身份用于对底层节点进行了适当的分类，上下文则决定了知识的存在环境。在城市规划上，透过网络和遥距监控技术，政府可充分掌握及分析城市的天气状况、资源运用的程度和道路交通状况等数据，因而调节及善用社区的资源，实现节能减排，减低“环境足迹”，提升环境的可持续性。围绕知识图谱的数据集成工作还可以支持创建新知识，可以在数据点之间建立联系，而这可能是以前一直未曾实现的。"
#         f"输出：（政府，透过，网络和遥距监控技术），（政府，掌握和分析，城市的天气状况、资源运用的程度和道路交通状况等数据），（政府，调节及善用，社区的资源），（政府，实现，节能减排），（政府，减低，“环境足迹”），（政府，提升，环境的可持续性）"
#         "示例结束\n"
#         "示例\n"
