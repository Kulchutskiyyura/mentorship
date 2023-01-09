from application import app
from application.server.services.text_analyzer import TextAnalyzer
from flask import request
from application.server.models import AnalysisReport


@app.route('/create', methods=["POST"])
def create_analyse_report():
    name = request.args.get('name')
    text = request.args.get('text')
    if not name and text:
        return None

    analyse_report = TextAnalyzer.get_report(name, text)
    analyse_report.save()

    return analyse_report.to_json()


@app.route('/get_analyse_report', methods=["GET"])
def get_analyse_report():
    name = request.args.get('name')
    if not name:
        return None

    return AnalysisReport.objects(name=name).first().to_json()


@app.route('/get_analyse_reports', methods=["GET"])
def get_analyse_reports():
    return AnalysisReport.objects().to_json()


@app.route('/', methods=["GET"])
def hello_words():
    return b'hello words'
