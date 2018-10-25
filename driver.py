from minimal_object_detection_lib import *

if __name__ == '__main__':
    # video_capture = WebcamVideoStream(0, width=480, height=360).start()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    objectDetector = MinimalObjectDetector()
    objectDetector.Initialize()
	
    while True:
        _, frame = cap.read()

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        result = objectDetector.Process(frame_rgb)
        
        print(json.dumps(result))

        # output_rgb = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
        # cv2.imshow('Video', output_rgb)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cap.release()
    # cv2.destroyAllWindows()
