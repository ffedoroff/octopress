---
layout: nil
---

{% for post in site.posts %}
if [ ! -f Biznes-sekrety/{{ post.english_short_title }}.mp3 ];
then
    echo {{ post.english_short_title }}.mp3 not found
fi
if [ ! -f Biznes-sekrety/{{ post.english_short_title }}.m4a ];
then
    echo {{ post.english_short_title }}.m4a not found
fi
{% endfor %}