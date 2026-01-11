import os
import shutil
import gradio as gr

def move_all_files(src_folder, dest_folder):
    if not os.path.exists(src_folder):
        return "Source folder does not exist."
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    moved_files = []
    for file_name in os.listdir(src_folder):
        src_path = os.path.join(src_folder, file_name)
        dest_path = os.path.join(dest_folder, file_name)

        # Skip folders, move only files
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
            moved_files.append(file_name)
    
    if moved_files:
        return f"Moved files:\n" + "\n".join(moved_files)
    else:
        return "No files found in the source folder."

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## File Mover")
    gr.Markdown("Select source and destination folders. All files from source will be moved to destination.")

    src_input = gr.Textbox(label="Source Folder Path")
    dest_input = gr.Textbox(label="Destination Folder Path")
    output_text = gr.Textbox(label="Result", lines=10)

    move_btn = gr.Button("Move Files")
    move_btn.click(
        move_all_files,
        inputs=[src_input, dest_input],
        outputs=output_text
    )

demo.launch()
