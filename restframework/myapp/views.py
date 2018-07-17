# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import PostForm

import operations

# Create your views here.


def post_new(request):
    form = PostForm()
    return render(request, 'blog/base.html', {'form': form})


def get_inputs(request):
    operations.get_asr()
