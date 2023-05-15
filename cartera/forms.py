from django import forms
import requests

class MiFormulario(forms.Form):
    url = "https://www.sistemapmn.com//api-app/internal/get-branch-office"
    payload = ""
    headers = {
        'Cookie': 'XSRF-TOKEN=eyJpdiI6Im5SWFpMTmNkOTBPM3pyZGNJcnhQc0E9PSIsInZhbHVlIjoiM3lnSk1NZ1pocEJmdm0yRVoxYUpZQnl2eG5uUDRcL3Vic0ZJQklWdXVvS3JmQVp1eSt1cldJYzlqUVV0bVNSYTFndkxSTWNkeVBGemdwXC9HRUdMOU9Tdz09IiwibWFjIjoiNWY1MTI3MzE1ZDQ0Y2YyODNhMDVjZjczOWQ3NjM3ODAxOWU5ZTI1MTIyMTc4MTU1ZWE2NjM3MDBlM2JiZDNjZCJ9; laravel_session=eyJpdiI6ImxHTHZvcE15Sm5oaGFqVkxkOHlqNkE9PSIsInZhbHVlIjoiQjV5V2YxUlBSQXZPZWVQQjYwejFhZGhncEZkQjBHamF0Nm85WnIrNU1YZW5PN010N2I0Um9JM0pWUGtTMHd4d1J6WTl4b2NyQkpmdnhGV3lkejZoXC93PT0iLCJtYWMiOiI3NWRmNDA2ODM1NWMzOGJlOTI4NjMyNzBkMjk2YzYwMzliZWIxYjRhMDFjNGQ3MjZjYWRjMzZmMzE2NjNmOGY0In0%3D'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    opciones = []

    for sucursal in data[0]:
        opciones.append((sucursal["sucursal_sucursales"], sucursal["sucursal_sucursales"]))

    combo_box = forms.ChoiceField(choices=opciones, widget=forms.Select(attrs={'class': 'form-control'}))
