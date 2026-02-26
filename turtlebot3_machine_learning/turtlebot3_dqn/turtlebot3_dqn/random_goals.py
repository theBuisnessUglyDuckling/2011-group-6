import os
import random
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity

class GoalSpawner(Node):

    def __init__(self):
        super().__init__('goal_spawner')

        self.client = self.create_client(SpawnEntity, '/spawn_entity')

        self.get_logger().info('Waiting for /spawn_entity service...')
        self.client.wait_for_service()
        self.get_logger().info('Service available. Spawning goals...')

        # Set the base path to your workspace models
        self.models_base_path = os.path.expanduser(
            '~/turtlebot3_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models'
        )

        self.spawn_goals()

    def spawn_model(self, name, model_path, x, y):
        request = SpawnEntity.Request()
        request.name = name

        if not os.path.isfile(model_path):
            self.get_logger().error(f'Model file not found: {model_path}')
            return

        with open(model_path, 'r') as f:
            request.xml = f.read()

        request.robot_namespace = ''
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = 0.03
        request.reference_frame = 'world'

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'Spawned {name}')
        else:
            self.get_logger().error(f'Failed to spawn {name}')

    def spawn_goals(self):
        num_red = random.randint(1, 5)
        num_blue = random.randint(1, 5)

        for i in range(num_red):
            x = random.uniform(-1.5, 1.5)
            y = random.uniform(-1.5, 1.5)

            red_model_path = os.path.join(self.models_base_path, 'Red_goal', 'model.sdf')
            self.spawn_model(f'red_goal_{i}', red_model_path, x, y)

        for i in range(num_blue):
            x = random.uniform(-1.5, 1.5)
            y = random.uniform(-1.5, 1.5)

            blue_model_path = os.path.join(self.models_base_path, 'Blue_goal', 'model.sdf')
            self.spawn_model(f'blue_goal_{i}', blue_model_path, x, y)

def main(args=None):
    rclpy.init(args=args)
    node = GoalSpawner()
    node.destroy_node()
    rclpy.shutdown()
