from rest_framework.views import APIView
from rest_framework.response import response
from .serializers import DishSerializer
class MenuView(APIView):
    def get(self,request):
        menu=[
            {"name:"Pasta","description":Creamy Alfredo Pasta","price":12.99}.
            {"name":"Pizza","description":"Cheese and tomato pizza","price":30}
        ]
        serializer=DishSerializer(menu,many=True)
        return Response(serializer.data)