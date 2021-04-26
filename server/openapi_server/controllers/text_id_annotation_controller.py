import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_id_annotation_request import TextIdAnnotationRequest  # noqa: E501
from openapi_server.models.text_id_annotation_response import TextIdAnnotationResponse  # noqa: E501
from openapi_server import util


def create_text_id_annotations(text_id_annotation_request=None):  # noqa: E501
    """Annotate IDs in a clinical note

    Return the ID annotations found in a clinical note # noqa: E501

    :param text_id_annotation_request: 
    :type text_id_annotation_request: dict | bytes

    :rtype: TextIdAnnotationResponse
    """
    if connexion.request.is_json:
        annotation_request = TextIdAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
        note = annotation_request._note
        print(note)
    return 'do some magic!'
