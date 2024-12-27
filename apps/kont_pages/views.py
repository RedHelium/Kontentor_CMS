from django.shortcuts import render
from django.views import View
from apps.kont_system.models import KontentorOpenGraphDataPage
from .models import KontentorPage, KontentorPageBlock
from django.http import Http404


class KontentorPageView(View):
    """
    Типовая страница сайта
    """

    def get(self, request, *args, **kwargs):

        slug = kwargs["slug"]

        get_params = request.GET
        add_slug = "/"

        if len(get_params) > 0:
            for param in get_params:
                add_slug += "<%s>" % (param)
            slug += add_slug

        page = KontentorPage.objects.filter(slug=slug, is_published=True).first()

        if page is None:
            raise Http404()

        open_graph = KontentorOpenGraphDataPage.objects.get(page=page)
        page_blocks = KontentorPageBlock.objects.filter(page=page, is_published=True)
        cross_page_blocks = KontentorPageBlock.objects.filter(
            is_cross_page_block=True, is_published=True
        )

        visible_blocks = page_blocks | cross_page_blocks

        rendered_pages = []

        for block in visible_blocks:
            rendered_pages.append(block.rendered_template(request))

        context = {"page": page, "open_graph": open_graph, "blocks": rendered_pages}

        return render(request, "page.html", context)

        # text = 'This is a sample text with [name] and [age] tags.'
        # pattern = r'\[(\w+)\]'
        # matches = re.findall(pattern, text)
        # data = {}
        # for match in matches:
        #     if "name" in match:
        #         data[match] = "JAY"
        #     else:
        #         data[match] = ''
