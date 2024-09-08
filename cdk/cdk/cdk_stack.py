from aws_cdk import (
    aws_ecs as ecs,
    aws_iam as iam,
    Stack,
)
from constructs import Construct

class MyEcsStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Fargate Task Definition
        task_definition = ecs.TaskDefinition(
            self, "MyECSTaskDefinition",
            compatibility=ecs.Compatibility.FARGATE,
            cpu="256",
            memory_mib="512"
        )

        # Add an execution role (required for Fargate tasks)
        execution_role = iam.Role(
            self, "TaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonECSTaskExecutionRolePolicy")
            ]
        )
        task_definition.execution_role = execution_role

        # Add a container to the task definition
        container = task_definition.add_container(
            "MyContainer",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            logging=ecs.LogDriver.aws_logs(stream_prefix="MyApp")
        )

        # Optionally, add port mappings
        container.add_port_mappings(
            ecs.PortMapping(
                container_port=80
            )
        )
