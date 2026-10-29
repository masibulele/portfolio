from flask import Flask, render_template


app= Flask(__name__)

PROJECTS = [
    {
        "title": "Gaming website",
        "image": "mockup2.mp4",
        "is_video": True,
        "github_url": "https://github.com/masibulele/stream_project",
        "demo_url": "https://gaming-hupu.onrender.com/",
    },
    {
        "title": "News website",
        "image": "mockup5.png",
        "github_url": "https://github.com/masibulele/news_website",
        "demo_url": "https://tech-news-puce.vercel.app/",
    },
    {
        "title": "infographic",
        "image": "mockup6.png",
        "github_url": "https://github.com/masibulele/results_component.git",
        "demo_url": "https://masibulele.github.io/results_component/",
    },
]



@app.route('/')
def home():

    return render_template('index.html', projects=PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)