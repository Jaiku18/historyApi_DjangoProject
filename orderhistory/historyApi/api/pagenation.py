from rest_framework.pagination import PageNumberPagination


class smallPagination(PageNumberPagination):
    page_size = 2
