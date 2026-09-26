from nicegui import ui
import back


table_data = ui.table(rows=back.fetch_data() or [], row_key="id", columns=[
    {"name":"col_date", "label":"Date", "field":"date"},
    {"name":"col_descript", "label":"Description", "field":"description"},
    {"name":"amount", "label":"Amount", "field":"amount"},
    {"name":"delete", "label":"Delete", "field":"delete"}
    ], column_defaults={
    'align': 'left',
    'headerClasses': 'uppercase text-primary',
}).classes("w-full")


def handle_delete(e):
    row_id = e.args
    back.delete_data(row_id)

    table_data.rows = back.fetch_data() or []
    table_data.update()

with table_data.add_slot("body-cell-delete"):
    with table_data.cell("delete"):
        ui.button(icon = "delete").on("click", handler=handle_delete, js_handler="() => emit(props.row.id)")


with ui.dialog() as dialog, ui.card().classes("w-106 p-6 gap-4 rounded-2xl"):
    raw_date = ui.date_input("Date", value="2026-09-24").classes("w-full")
    raw_description = ui.input(label="Description", placeholder="type here").classes("w-full")
    raw_amount = ui.input(label =  "label", placeholder="type here").classes("w-full")

    def adding():
        back.add_expenses(date = raw_date.value, description = raw_description.value, amount = raw_amount.value)
        table_data.rows = back.fetch_data() or []
        table_data.update()
        dialog.close()

    with ui.row().classes("w-full justify-end gap-3"):
        ui.button("cancel", on_click=dialog.close)
        ui.button("Add", on_click = adding
    )
ui.button("Open", on_click=dialog.open)


ui.run()
