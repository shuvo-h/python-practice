from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'  # 'limit' query parameter will control the page size
    max_page_size = 100

class PostListCreateView(generics.GenericAPIView):
    pagination_class = CustomPagination
    

    def get(self, request, *args, **kwargs):
        """Handle GET requests (list static posts with pagination, limit, and search)."""
        # Static data (fake posts)
        posts = [
            {"id": 1, "title": "First Post", "content": "Content of the first post", "author": 1},
            {"id": 2, "title": "Second Post", "content": "Content of the second post", "author": 1},
            {"id": 3, "title": "Third Post", "content": "Content of the third post", "author": 2},
            {"id": 4, "title": "Fourth Post", "content": "Content of the fourth post", "author": 2},
            {"id": 5, "title": "Fifth Post", "content": "Content of the fifth post", "author": 3},
            {"id": 6, "title": "Sixth Post", "content": "Content of the sixth post", "author": 3},
            {"id": 7, "title": "Seventh Post", "content": "Content of the seventh post", "author": 1},
            {"id": 8, "title": "Eighth Post", "content": "Content of the eighth post", "author": 2}
        ]

        # Search logic (query param 'q')
        search_query = request.query_params.get('q', None)
        if search_query:
            posts = [post for post in posts if search_query.lower() in post['title'].lower()]

        # Paginate the static data
        page = self.paginate_queryset(posts)
        if page is not None:
            return self.get_paginated_response({
                "success": True,
                "message": "Static posts fetched successfully",
                "posts": page
            })

        return Response({
            "success": True,
            "message": "Static posts fetched successfully",
            "posts": posts
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handle POST requests (create post - mock response)."""
        return Response({
            "success": True,
            "message": "Static post created successfully",
            "data": request.data  # Return the same data for mock purposes
        }, status=status.HTTP_201_CREATED)

class PostDetailView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        """Handle GET requests (retrieve static post details)."""
        post_id = kwargs.get('pk')
        # Static post data
        posts = [
            {"id": 1, "title": "First Post", "content": "Content of the first post", "author": 1},
            {"id": 2, "title": "Second Post", "content": "Content of the second post", "author": 1},
            {"id": 3, "title": "Third Post", "content": "Content of the third post", "author": 2},
        ]
        post = next((post for post in posts if post["id"] == int(post_id)), None)

        if post:
            return Response({
                "success": True,
                "message": "Static post retrieved successfully",
                "data": post
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "success": False,
                "message": "Post not found"
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        """Handle PUT requests (update post - mock response)."""
        return Response({
            "success": True,
            "message": "Static post updated successfully",
            "data": request.data  # Return updated data for mock purposes
        }, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """Handle DELETE requests (delete post - mock response)."""
        return Response({
            "success": True,
            "message": "Static post deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
