def draw_gantt_chart(canvas, gantt_data):
    canvas.delete("all")
    start_x = 20
    y = 50
    height = 30
    scale = 30
    for entry in gantt_data:
        process = entry['process']
        start = entry['start']
        end = entry['end']
        width = (end - start) * scale
        canvas.create_rectangle(start_x + start * scale, y,
                               start_x + start * scale + width, y + height,
                               fill='skyblue')
        canvas.create_text(start_x + start * scale + width / 2, y + height / 2, text=process)
        canvas.create_text(start_x + start * scale, y + height + 15, text=str(start))
        canvas.create_text(start_x + start * scale + width, y + height + 15, text=str(end))
