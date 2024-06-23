from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint = "<your-endpoint>"
key = "<your-key>"

docUrl = "<url-of-document-to-analyze>"

document_analysis_client = DocumentIntelligenceClient(endpoint=endpoint,
    credential=AzureKeyCredential(key))

poller = document_analysis_client.begin_analyze_document_from_url(
    "prebuilt-document", docUrl)
result: AnalyzeResult = poller.result()
