import os
from xml.sax.saxutils import escape

from flask import Flask, Response, render_template, url_for
from projects import PROJECTS

app = Flask(__name__)


def get_site_url():
    return os.environ.get("SITE_URL", url_for("home", _external=True)).rstrip("/")


@app.route('/')
def home():
    site_url = get_site_url()
    return render_template(
        'index.html',
        projects=PROJECTS,
        site_url=site_url,
        social_image=f"{site_url}{url_for('static', filename='assets/Masi_smoke.png')}",
    )


@app.route('/robots.txt')
def robots():
    content = f"User-agent: *\nAllow: /\nSitemap: {get_site_url()}/sitemap.xml\n"
    return Response(content, mimetype='text/plain')


@app.route('/sitemap.xml')
def sitemap():
    site_url = escape(get_site_url())
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{site_url}/</loc></url>\n'
        '</urlset>\n'
    )
    return Response(content, mimetype='application/xml')


if __name__ == '__main__':
    app.run()
