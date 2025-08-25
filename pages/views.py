from django.shortcuts import render

# Create your views here.

def home(request):
    
    content = {
        "latest_posts": [
            {
                "title": "This is a post",
                "url":  "",
                "first_published_at": "01/12/2020",
                "preview_image": "https://static.wixstatic.com/media/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png/v1/fill/w_342,h_342,fp_0.50_0.50,q_95,enc_avif,quality_auto/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png",
                "owner": {
                    "username": "Hearthlight",
                    "get_full_name": "Hearthlight"
                },
                "likes": 10,
                "views": 14
            },
            {
                "title": "This is a post",
                "url":  "",
                "first_published_at": "01/12/2020",
                "preview_image": "https://static.wixstatic.com/media/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png/v1/fill/w_342,h_342,fp_0.50_0.50,q_95,enc_avif,quality_auto/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png",
                "owner": {
                    "username": "Hearthlight",
                    "get_full_name": "Hearthlight"
                },
                "likes": 10,
                "views": 14
            }
        ],
    }


    return render(request, "pages/home.html", content)

def base(request):

    content = {
        "latest_posts": [
            {
                "title": "This is a post",
                "url":  "",
                "first_published_at": "01/12/2020",
                "preview_image": "https://static.wixstatic.com/media/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png/v1/fill/w_342,h_342,fp_0.50_0.50,q_95,enc_avif,quality_auto/2d36ac_6ff5eb6e723e44d08ea36a69149667d0~mv2.png",
                "owner": {
                    "username": "Hearthlight",
                    "get_full_name": "Hearthlight"
                },
                "likes": 10,
                "views": 14
            }
        ],
    }

    return render(request, "pages/test-page.html", content)