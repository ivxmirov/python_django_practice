from foodgram import constants
from rest_framework.pagination import PageNumberPagination


class CustomLimitPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = constants.PAGE_SIZE
