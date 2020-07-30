# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ReplicationTask']


class ReplicationTask(pulumi.CustomResource):
    cdc_start_time: pulumi.Output[Optional[str]] = pulumi.output_property("cdcStartTime")
    """
    The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.
    """
    migration_type: pulumi.Output[str] = pulumi.output_property("migrationType")
    """
    The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.
    """
    replication_instance_arn: pulumi.Output[str] = pulumi.output_property("replicationInstanceArn")
    """
    The Amazon Resource Name (ARN) of the replication instance.
    """
    replication_task_arn: pulumi.Output[str] = pulumi.output_property("replicationTaskArn")
    """
    The Amazon Resource Name (ARN) for the replication task.
    """
    replication_task_id: pulumi.Output[str] = pulumi.output_property("replicationTaskId")
    """
    The replication task identifier.
    """
    replication_task_settings: pulumi.Output[Optional[str]] = pulumi.output_property("replicationTaskSettings")
    """
    An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).
    """
    source_endpoint_arn: pulumi.Output[str] = pulumi.output_property("sourceEndpointArn")
    """
    The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.
    """
    table_mappings: pulumi.Output[str] = pulumi.output_property("tableMappings")
    """
    An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the resource.
    """
    target_endpoint_arn: pulumi.Output[str] = pulumi.output_property("targetEndpointArn")
    """
    The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, cdc_start_time: Optional[pulumi.Input[str]] = None, migration_type: Optional[pulumi.Input[str]] = None, replication_instance_arn: Optional[pulumi.Input[str]] = None, replication_task_id: Optional[pulumi.Input[str]] = None, replication_task_settings: Optional[pulumi.Input[str]] = None, source_endpoint_arn: Optional[pulumi.Input[str]] = None, table_mappings: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, target_endpoint_arn: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Provides a DMS (Data Migration Service) replication task resource. DMS replication tasks can be created, updated, deleted, and imported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new replication task
        test = aws.dms.ReplicationTask("test",
            cdc_start_time=1484346880,
            migration_type="full-load",
            replication_instance_arn=aws_dms_replication_instance["test-dms-replication-instance-tf"]["replication_instance_arn"],
            replication_task_id="test-dms-replication-task-tf",
            replication_task_settings="...",
            source_endpoint_arn=aws_dms_endpoint["test-dms-source-endpoint-tf"]["endpoint_arn"],
            table_mappings="{\"rules\":[{\"rule-type\":\"selection\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"object-locator\":{\"schema-name\":\"%\",\"table-name\":\"%\"},\"rule-action\":\"include\"}]}",
            tags={
                "Name": "test",
            },
            target_endpoint_arn=aws_dms_endpoint["test-dms-target-endpoint-tf"]["endpoint_arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cdc_start_time: The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.
        :param pulumi.Input[str] migration_type: The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.
        :param pulumi.Input[str] replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param pulumi.Input[str] replication_task_id: The replication task identifier.
        :param pulumi.Input[str] replication_task_settings: An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).
        :param pulumi.Input[str] source_endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.
        :param pulumi.Input[str] table_mappings: An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] target_endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['cdc_start_time'] = cdc_start_time
            if migration_type is None:
                raise TypeError("Missing required property 'migration_type'")
            __props__['migration_type'] = migration_type
            if replication_instance_arn is None:
                raise TypeError("Missing required property 'replication_instance_arn'")
            __props__['replication_instance_arn'] = replication_instance_arn
            if replication_task_id is None:
                raise TypeError("Missing required property 'replication_task_id'")
            __props__['replication_task_id'] = replication_task_id
            __props__['replication_task_settings'] = replication_task_settings
            if source_endpoint_arn is None:
                raise TypeError("Missing required property 'source_endpoint_arn'")
            __props__['source_endpoint_arn'] = source_endpoint_arn
            if table_mappings is None:
                raise TypeError("Missing required property 'table_mappings'")
            __props__['table_mappings'] = table_mappings
            __props__['tags'] = tags
            if target_endpoint_arn is None:
                raise TypeError("Missing required property 'target_endpoint_arn'")
            __props__['target_endpoint_arn'] = target_endpoint_arn
            __props__['replication_task_arn'] = None
        super(ReplicationTask, __self__).__init__(
            'aws:dms/replicationTask:ReplicationTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, cdc_start_time: Optional[pulumi.Input[str]] = None, migration_type: Optional[pulumi.Input[str]] = None, replication_instance_arn: Optional[pulumi.Input[str]] = None, replication_task_arn: Optional[pulumi.Input[str]] = None, replication_task_id: Optional[pulumi.Input[str]] = None, replication_task_settings: Optional[pulumi.Input[str]] = None, source_endpoint_arn: Optional[pulumi.Input[str]] = None, table_mappings: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, target_endpoint_arn: Optional[pulumi.Input[str]] = None) -> 'ReplicationTask':
        """
        Get an existing ReplicationTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cdc_start_time: The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.
        :param pulumi.Input[str] migration_type: The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.
        :param pulumi.Input[str] replication_instance_arn: The Amazon Resource Name (ARN) of the replication instance.
        :param pulumi.Input[str] replication_task_arn: The Amazon Resource Name (ARN) for the replication task.
        :param pulumi.Input[str] replication_task_id: The replication task identifier.
        :param pulumi.Input[str] replication_task_settings: An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).
        :param pulumi.Input[str] source_endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.
        :param pulumi.Input[str] table_mappings: An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] target_endpoint_arn: The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cdc_start_time"] = cdc_start_time
        __props__["migration_type"] = migration_type
        __props__["replication_instance_arn"] = replication_instance_arn
        __props__["replication_task_arn"] = replication_task_arn
        __props__["replication_task_id"] = replication_task_id
        __props__["replication_task_settings"] = replication_task_settings
        __props__["source_endpoint_arn"] = source_endpoint_arn
        __props__["table_mappings"] = table_mappings
        __props__["tags"] = tags
        __props__["target_endpoint_arn"] = target_endpoint_arn
        return ReplicationTask(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

