from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Portfolio
from .serializers import RegisterSerializer, UserProfileSerializer, PortfolioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.portfolios.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total = 0
        for pf in request.user.portfolios.all():
            for ps in pf.portfoliostock_set.all():
                total += ps.quantity * ps.stock.current_price
            for mf in pf.portfoliomutualfund_set.all():
                total += mf.units * mf.mutual_fund.current_nav

        # mock profit
        return Response({"total_investment": total, "profit": 0})
