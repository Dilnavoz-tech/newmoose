from django.shortcuts import render, redirect
from .models import Post, Contact, Comment
from django.core.paginator import Paginator
import requests
BOT_TOKEN = '7021912578:AAEQDKadKXeTUrJY8jW4L6A5h23_EOVytZI'
CHAT_ID = '1806940376'

def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-view_count')[:2 ]
    d = {
        'posts': posts,
        'home': 'active'
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    return render(request, 'about.html', context={'about': 'active'})


def blog_details_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post_id=pk, is_visible=True)
    d = {
        'post': post,
        'comments': comments,
        'comments_count': len(comments),
        'blog': 'active'

    }
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(full_name=data['full_name'], email=data['email'],
                                     message=data['message'], post_id=pk)
        obj.save()
        return redirect(f'/blog/{pk}')
    post.view_count += 1
    post.save(update_fields=['view_count'])

    return render(request, 'blog-single.html', context=d)


def blog_view(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
        d = {
            'posts': posts,
            'blog': 'active',
        }
        return render(request, 'blog.html', context=d)

    posts = Post.objects.filter(is_published=True)
    page_obj = Paginator(posts, 2)
    d = {
        'blog': 'active',
        'posts': page_obj.get_page(page)
    }
    return render(request, 'blog.html', context=d)



def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data['name'], email=data['email'],
                                     subject=data['subject'], message=data['message'])
        obj.save()
        text = f'''
        project: MOOSE
        id: {obj.id}
        name: {obj.name}
        subject: {obj.subject}
        message: {obj.message}
        timestamp: {obj.created_at}
        '''
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
        response = requests.get(url)
        print(response)
        return redirect('/contact')
    return render(request, 'contact.html', context={'contact': 'active'})


