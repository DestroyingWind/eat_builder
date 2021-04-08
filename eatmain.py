import multiprocessing as mp

from FlaskPart import app, real_build

p0 = mp.Process(target=app.run, args=('0.0.0.0', 5001))
p1 = mp.Process(target=real_build)
if __name__ == "__main__":
    p0.start()
    p1.start()
