from nicegui import ui


ui.table(rows=[
    {"date":2026, "description":"lunch", "amount":130},
    {"date":2026, "description":"jeep fee", "amount":450},
    {"date":2026, "description":"eletric bill", "amount":3500},
], columns=[
    {"name":"col_date", "label":"Date", "field":"date"},
    {"name":"col_descript", "label":"Description", "field":"description"},
    {"name":"amount", "label":"Amount", "field":"amount"},
], column_defaults={
    'align': 'left',
    'headerClasses': 'uppercase text-primary',
}).classes("w-full")


with ui.dialog() as dialog, ui.card().classes("w-106 p-6 gap-4 rounded-2xl"):
    date = ui.date_input("Date", value="2026-09-24").classes("w-full")
    description = ui.input(label="Description", placeholder="type here").classes("w-full")
    amount = ui.input(label =  "label", placeholder="type here").classes("w-full")

    with ui.row().classes("w-full justify-end gap-3"):
        ui.button("cancel", on_click=dialog.close)
        ui.button("Add")
ui.button("Open", on_click=dialog.open)


ui.run()
