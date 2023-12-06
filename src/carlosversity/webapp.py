import gradio as gr
from carlosversity import pipeline

predict = pipeline()

with gr.Blocks(title="carlosversity") as webapp:
    gr.Markdown("# Greetings from carlosversity!")
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()

    inp.change(fn=predict,
               inputs=inp,
               outputs=out)