for image in testio/detect_obstacles/*.in.png
do
  echo ./detect_obstacles.py "$image" "testio/detect_obstacles/$(basename "$image" .in.png).out.png"
  ./detect_obstacles.py "$image" "testio/detect_obstacles/$(basename "$image" .in.png).out.png"
done
