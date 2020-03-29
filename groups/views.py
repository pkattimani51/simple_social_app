from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Group, GroupMember
from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError


class SingleGroup(generic.DetailView):
    model = Group


class ListGroup(generic.ListView):
    model = Group


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    fields = ('name', 'description')


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))
        print(group)
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, "Warning, You are already member of {}".format(group.name))
        except Exception as e:
            print(str(e))
        else:
            messages.success(self.request, "You are now member of {} group".format(group.name))
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get("slug")})


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug'))
        except GroupMember.DoesNotExist:
            messages.warning(self.request, "You cannot leave this group, because you are not a part of this")
        else:
            membership.delete()
            messages.success(self.request, "You are successfully left the group")
        return super().get(request, *args, **kwargs)
