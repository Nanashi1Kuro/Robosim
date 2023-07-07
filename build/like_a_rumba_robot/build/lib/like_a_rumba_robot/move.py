import time 
 
from geometry_msgs.msg import PoseStamped 
from rclpy.duration import Duration 
import rclpy 
 
from .robot_navigator import BasicNavigator, NavigationResult
 

def main():
 
  rclpy.init()
 
  navigator = BasicNavigator()
 
  navigator.waitUntilNav2Active()
  
  goal_pose = [PoseStamped() for i in range(15)]
  
  goal_pose[0].header.frame_id = 'map'
  goal_pose[0].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[0].pose.position.x = -0.012
  goal_pose[0].pose.position.y = 1.30
  goal_pose[0].pose.position.z = 0.0
  goal_pose[0].pose.orientation.x = 0.0
  goal_pose[0].pose.orientation.y = 0.0
  goal_pose[0].pose.orientation.z = 1.57
  goal_pose[0].pose.orientation.w = 1.0
  
  goal_pose[1].header.frame_id = 'map'
  goal_pose[1].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[1].pose.position.x = -1.03
  goal_pose[1].pose.position.y = 1.30
  goal_pose[1].pose.position.z = 0.0
  goal_pose[1].pose.orientation.x = 0.0
  goal_pose[1].pose.orientation.y = 0.0
  goal_pose[1].pose.orientation.z = 3.14
  goal_pose[1].pose.orientation.w = 1.0
  
  goal_pose[2].header.frame_id = 'map'
  goal_pose[2].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[2].pose.position.x = -1.03
  goal_pose[2].pose.position.y = 1.96
  goal_pose[2].pose.position.z = 0.0
  goal_pose[2].pose.orientation.x = 0.0
  goal_pose[2].pose.orientation.y = 0.0
  goal_pose[2].pose.orientation.z = 1.57
  goal_pose[2].pose.orientation.w = 1.0
  
  goal_pose[3].header.frame_id = 'map'
  goal_pose[3].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[3].pose.position.x = 1.97
  goal_pose[3].pose.position.y = 1.97
  goal_pose[3].pose.position.z = 0.0
  goal_pose[3].pose.orientation.x = 0.0
  goal_pose[3].pose.orientation.y = 0.0
  goal_pose[3].pose.orientation.z = 0.0
  goal_pose[3].pose.orientation.w = 1.0
  
  goal_pose[4].header.frame_id = 'map'
  goal_pose[4].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[4].pose.position.x = 4.57
  goal_pose[4].pose.position.y = 1.99
  goal_pose[4].pose.position.z = 0.0
  goal_pose[4].pose.orientation.x = 0.0
  goal_pose[4].pose.orientation.y = 0.0
  goal_pose[4].pose.orientation.z = 0.0
  goal_pose[4].pose.orientation.w = 1.0
  
  goal_pose[5].header.frame_id = 'map'
  goal_pose[5].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[5].pose.position.x = 4.62
  goal_pose[5].pose.position.y = 2.96
  goal_pose[5].pose.position.z = 0.0
  goal_pose[5].pose.orientation.x = 0.0
  goal_pose[5].pose.orientation.y = 0.0
  goal_pose[5].pose.orientation.z = 1.57
  goal_pose[5].pose.orientation.w = 1.0
  
  goal_pose[6].header.frame_id = 'map'
  goal_pose[6].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[6].pose.position.x = 1.96
  goal_pose[6].pose.position.y = 2.96
  goal_pose[6].pose.position.z = 0.0
  goal_pose[6].pose.orientation.x = 0.0
  goal_pose[6].pose.orientation.y = 0.0
  goal_pose[6].pose.orientation.z = 3.14
  goal_pose[6].pose.orientation.w = 1.0
 
  goal_pose[7].header.frame_id = 'map'
  goal_pose[7].header.stamp = navigator.get_clock().now().to_msg() 
  goal_pose[7].pose.position.x = -1.01
  goal_pose[7].pose.position.y = 2.97
  goal_pose[7].pose.position.z = 0.0
  goal_pose[7].pose.orientation.x = 0.0
  goal_pose[7].pose.orientation.y = 0.0
  goal_pose[7].pose.orientation.z = 3.14
  goal_pose[7].pose.orientation.w = 1.0
  
  goal_pose[8].header.frame_id = 'map'
  goal_pose[8].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[8].pose.position.x = -1.01
  goal_pose[8].pose.position.y = 2.97
  goal_pose[8].pose.position.z = 0.0
  goal_pose[8].pose.orientation.x = 0.0
  goal_pose[8].pose.orientation.y = 0.0
  goal_pose[8].pose.orientation.z = 1.57
  goal_pose[8].pose.orientation.w = 1.0
  
  
  goal_pose[9].header.frame_id = 'map'
  goal_pose[9].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[9].pose.position.x = -1.00
  goal_pose[9].pose.position.y = 3.98
  goal_pose[9].pose.position.z = 0.0
  goal_pose[9].pose.orientation.x = 0.0
  goal_pose[9].pose.orientation.y = 0.0
  goal_pose[9].pose.orientation.z = 1.57
  goal_pose[9].pose.orientation.w = 1.0
  
  goal_pose[10].header.frame_id = 'map'
  goal_pose[10].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[10].pose.position.x = 1.96
  goal_pose[10].pose.position.y = 3.96
  goal_pose[10].pose.position.z = 0.0
  goal_pose[10].pose.orientation.x = 0.0
  goal_pose[10].pose.orientation.y = 0.0
  goal_pose[10].pose.orientation.z = 0.0
  goal_pose[10].pose.orientation.w = 1.0
  
  goal_pose[11].header.frame_id = 'map'
  goal_pose[11].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[11].pose.position.x = 4.53
  goal_pose[11].pose.position.y = 3.99
  goal_pose[11].pose.position.z = 0.0
  goal_pose[11].pose.orientation.x = 0.0
  goal_pose[11].pose.orientation.y = 0.0
  goal_pose[11].pose.orientation.z = 0.0
  goal_pose[11].pose.orientation.w = 1.0
  
  goal_pose[12].header.frame_id = 'map'
  goal_pose[12].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[12].pose.position.x = 0.0
  goal_pose[12].pose.position.y = 0.0
  goal_pose[12].pose.position.z = 0.0
  goal_pose[12].pose.orientation.x = 0.0
  goal_pose[12].pose.orientation.y = 0.0
  goal_pose[12].pose.orientation.z = 0.0
  goal_pose[12].pose.orientation.w = 1.0
  """
  goal_pose[12].header.frame_id = 'map'
  goal_pose[12].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[12].pose.position.x = 1.41
  goal_pose[12].pose.position.y = -1.0
  goal_pose[12].pose.position.z = 0.0
  goal_pose[12].pose.orientation.x = 0.0
  goal_pose[12].pose.orientation.y = 0.0
  goal_pose[12].pose.orientation.z = 0.0
  goal_pose[12].pose.orientation.w = 1.0
  
  goal_pose[13].header.frame_id = 'map'
  goal_pose[13].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[13].pose.position.x = -2.0
  goal_pose[13].pose.position.y = -1.67
  goal_pose[13].pose.position.z = 0.0
  goal_pose[13].pose.orientation.x = 0.0
  goal_pose[13].pose.orientation.y = 0.0
  goal_pose[13].pose.orientation.z = 0.0
  goal_pose[13].pose.orientation.w = 1.0
  
  goal_pose[14].header.frame_id = 'map'
  goal_pose[14].header.stamp = navigator.get_clock().now().to_msg()
  goal_pose[14].pose.position.x = -0.98
  goal_pose[14].pose.position.y = -4.86
  goal_pose[14].pose.position.z = 0.0
  goal_pose[14].pose.orientation.x = 0.0
  goal_pose[14].pose.orientation.y = 0.0
  goal_pose[14].pose.orientation.z = 0.0
  goal_pose[14].pose.orientation.w = 1.0
  """
  print("Waiting 10 seconds until everything is up")
  time.sleep(10);
  #path = navigator.getPath(initial_pose, goal_pose)
  for i in range(0,13):
      print("---------------------------------------GOAL "+ str(i)+"------------------------------")
      navigator.goToPose(goal_pose[i])
 
      i = 0
      
      while not navigator.isNavComplete():

        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
          print('Distance remaining: ' + '{:.2f}'.format(
          feedback.distance_remaining) + ' meters.')
 
      result = navigator.getResult()
      if result == NavigationResult.SUCCEEDED:
          print('Goal succeeded!')
      elif result == NavigationResult.CANCELED:
         print('Goal was canceled!')
      elif result == NavigationResult.FAILED:
         print('Goal failed!')
      else:
          print('Goal has an invalid return status!')
 
  navigator.lifecycleShutdown()
 
  exit(0)
 
if __name__ == '__main__':
  main()
