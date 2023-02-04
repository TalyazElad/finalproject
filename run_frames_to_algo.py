import os
import sys
import subprocess
import concurrent.futures

frame_path = "C:\\Users\\eladtal\\PycharmProjects\\pythonProject1\\1MB"
script_path = "C:\\Users\\eladtal\\PycharmProjects\\pythonProject1\\finalproject"

def get_frame_grade(frame):
    cmd = [sys.executable, os.path.join(script_path, 'test.py'), '--mode', 'piqe', '--path', frame]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    score = float(output.split("-----piqe score:")[1])
    return score

def average_grades(frames):
    total_grade = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_frame = {executor.submit(get_frame_grade, frame): frame for frame in frames}
        for future in concurrent.futures.as_completed(future_to_frame):
            frame = future_to_frame[future]
            try:
                grade = future.result()
                print(grade)
                total_grade += grade
            except Exception as exc:
                print(f'{frame} generated an exception: {exc}')
    return total_grade / len(frames)

if __name__ == '__main__':
    frames = [f'frame{i}.jpg' for i in range(35,1671)]
    avg_grade = average_grades(frames)
    print(f'Average grade: {avg_grade}')
