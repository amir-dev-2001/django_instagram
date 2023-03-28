from django.views import View
from django.contrib.auth import get_user_model
from django.http import Http404
from relation.models import Relation
from django.shortcuts import redirect

User = get_user_model()

class FollowView(View):
    pattern_name = 'profile'

    def get_object(self):
        try:
            user = User.objects.get(username=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        return user            

    def post(self, request, *args, **kwargs):
        target_user = self.get_object()
        querySet = Relation.objects.filter(from_user=request.user, to_user=target_user)
        if querySet.exists():
            querySet.delete()
        else:
            Relation.objects.create(from_user=request.user, to_user=target_user)
        return redirect('/{}/'.format(target_user.username))
