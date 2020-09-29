import scrapy


def clean_text(txt):
    txt.replace("\n", "")
    txt.replace("\r", "")
    txt.replace("xa0", "")
    return txt


class QuotesSpider(scrapy.Spider):
    name = "topdoctor"

    def start_requests(self):
        urls = [
            'https://www.topdoctors.com.co/doctor/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath("//a[@class='h3 item_name']/@href").getall()
        for link in links:
            yield scrapy.Request(
                url=response.urljoin(link),
                callback=self.parse_doctorprofile
            )

        pages_url = response.css(".pagination a::attr(href)").getall()[-4:-1]
        for page in pages_url:
            yield scrapy.Request(
                url=response.urljoin(page),
                callback=self.parse,
            )


    def parse_doctorprofile(self, response):
        name = ' '.join(response.xpath("//h1//span[@itemprop='name']/text()").get().strip().split()[1:])
        name_op2 = response.css('title::text').get().split(':')[0]
        if response.xpath("//section[@id='profile_header_title']//p[@class='hidden-xs text-muted']/text()").get():
            id_profesional = response.xpath("//section[@id='profile_header_title']//p[@class='hidden-xs text-muted']/text()").get().strip()
        else:
            id_profesional = ''
        profession = response.css('title::text').get().split()[-3].capitalize()
        if len(profession) < 3:
            profession = response.xpath("//section[@id='profile_header_title']//h2//a/text()").get().strip()
        link_career = response.xpath("//section[@id='profile_header_title']//a/@href").get()  # https://www.topdoctors.com.co/psicologia/
        specialities = ', '.join(response.xpath("//section[@class='content_highlight']//ul//li[@class='item']//a/text()").getall())
        if response.xpath("//section[@id='profile_header_title']//h2//a/text()").getall()[0].strip() != profession:
            info = response.xpath("//section[@id='profile_header_title']//h2//a/text()").getall()[0].strip()
        else:
            info = ''
        about = ''.join(response.css("section.item_description p *::text").getall()).strip()
        address = response.xpath("//meta[@itemprop='streetAddress']/@content").get()
        city = response.xpath("//section[@id='profile_header_title']//h2//a/text()").getall()[-1].strip()
        telephone = response.xpath("//meta[@itemprop='telephone']/@content").get()
        instagram = response.xpath("//a[re:test(@href, 'instagram')]/@href").get()
        facebook = response.xpath("//a[re:test(@href, 'facebook')]/@href").get()
        if 'topdoctors' in instagram:
            instagram = ''
        if 'topdoctors' in facebook:
            facebook = ''
            pass

        yield{
            'name': name,
            'id_profesional': id_profesional,
            'profession': profession,
            'specialities': specialities,
            'info': info,
            'about': about,
            # 'link_career': link_career,
            'address': address,
            'city': city,
            'telephone': telephone,
            'instagram': instagram,
            'facebook': facebook,
            'url': response.url
        }


