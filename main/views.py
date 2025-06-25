from django.shortcuts import render
from django.db import connection

def index(request):
    selected_category = request.GET.get('category')
    selected_table = request.GET.get('table')
    headers, rows = [], []

    bhavcopy_tables = [
        "bc_records", "bh_records", "corpbond_records", "etf_records",
        "gl_records", "hl_records", "mcap_records", "pd_records",
        "pr_records", "sme_records", "tt_records"
    ]

    if selected_category == 'bhavcopy' and selected_table in bhavcopy_tables:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"SELECT * FROM `{selected_table}`")
                headers = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
            except Exception as e:
                print("Database error:", e)

    context = {
        'selected_category': selected_category,
        'selected_table': selected_table,
        'bhavcopy_tables': bhavcopy_tables,
        'headers': headers,
        'rows': rows,
    }
    return render(request, 'index.html', context)
