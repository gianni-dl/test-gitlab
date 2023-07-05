#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

{
    "name": "Product Related Questions",
    "version": "16.0.2.0.0",
    "summary": "Link products to the questions on the crm form in the website.",
    "category": "Sales/CRM",
    "author": "Gumbys NV",
    "website": "https://gumbys.be",
    "license": "OEEL-1",
    "depends": ["sale_crm", "website_crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_related_question_views.xml",
        "views/product_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
