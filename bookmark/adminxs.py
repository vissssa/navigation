from django.utils.safestring import mark_safe


class BookMarkAdminx:

    def show_pic(self, obj):
        html = "<div align='center'><img src='%s' width='45' height='45'></div>" % obj.pic
        return mark_safe(html)

    show_pic.short_description = mark_safe("<p align='center' style='color:#428BCA'>图片</p>")

    def show_name(self, obj):
        html = "<div align='center'>%s</div>" % obj.name
        return mark_safe(html)

    show_name.short_description = mark_safe("<p align='center' style='color:#428BCA'>名称</p>")

    def show_desc(self, obj):
        html = "<div align='center'>%s</div>" % obj.desc
        return mark_safe(html)

    show_desc.short_description = mark_safe("<p align='center' style='color:#428BCA'>描述</p>")

    def show_url(self, obj):
        html = "<div align='center'>%s</div>" % obj.url
        return mark_safe(html)

    show_url.short_description = mark_safe("<p align='center' style='color:#428BCA'>链接</p>")

    def show_tag(self, obj):
        html = "<div align='center'>%s</div>" % obj.tag
        return mark_safe(html)

    show_tag.short_description = mark_safe("<p align='center' style='color:#428BCA'>标签</p>")

    def deploy(self, request, queryset):
        template_product = ''
        template_bookmark = ''
        template_docs = ''

        list_bookmark = []

        from bookmark.models import BookMark
        bookmarks = BookMark.objects.all()
        for bookmark in bookmarks:
            raw = {'name': bookmark.name, 'desc': bookmark.desc, 'pic': bookmark.pic, 'url': bookmark.url,
                   'tag': bookmark.tag}
            list_bookmark.append(raw)

        for dict_bookmark in list_bookmark:
            if dict_bookmark['tag'] == 'product':
                template_product += f'''<a target="_blank" href="{dict_bookmark['url']}">
                                <div class="item">
                                    <div class="logo"><img src="{dict_bookmark['pic']}" alt="blog"> {dict_bookmark[
                    'name']}</div>
                                    <div class="desc"> {dict_bookmark['desc']}</div>
                                </div>
                            </a>'''
            elif dict_bookmark['tag'] == 'bookmark':
                template_bookmark += f'''<a target="_blank" href="{dict_bookmark['url']}">
                                <div class="item">
                                    <div class="logo"><img src="{dict_bookmark['pic']}" alt="blog"> {dict_bookmark[
                    'name']}</div>
                                    <div class="desc"> {dict_bookmark['desc']}</div>
                                </div>
                            </a>'''
            elif dict_bookmark['tag'] == 'docs':
                template_docs += f'''<a target="_blank" href="{dict_bookmark['url']}">
                                <div class="item">
                                    <div class="logo"><img src="{dict_bookmark['pic']}" alt="blog"> {dict_bookmark[
                    'name']}</div>
                                    <div class="desc"> {dict_bookmark['desc']}</div>
                                </div>
                            </a>'''

        with open('/home/zhangyu/web/navigation/template.html', 'r') as f:
            html = f.read()
            html = html.replace('{{product}}', template_product).replace('{{bookmark}}', template_bookmark).replace(
                '{{docs}}', template_docs)

        with open('/home/zhangyu/web/navigation/index.html', 'w') as f:
            f.write(html if html else '')

    deploy.short_description = '开始部署'

    fields = ('name', 'desc', 'url', 'pic', 'tag')
    list_display = ['show_pic', 'show_name', 'show_desc', 'show_url', 'show_tag']
    actions = ['deploy']
