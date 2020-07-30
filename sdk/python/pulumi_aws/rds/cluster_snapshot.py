# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ClusterSnapshot']


class ClusterSnapshot(pulumi.CustomResource):
    allocated_storage: pulumi.Output[float] = pulumi.output_property("allocatedStorage")
    """
    Specifies the allocated storage size in gigabytes (GB).
    """
    availability_zones: pulumi.Output[List[str]] = pulumi.output_property("availabilityZones")
    """
    List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
    """
    db_cluster_identifier: pulumi.Output[str] = pulumi.output_property("dbClusterIdentifier")
    """
    The DB Cluster Identifier from which to take the snapshot.
    """
    db_cluster_snapshot_arn: pulumi.Output[str] = pulumi.output_property("dbClusterSnapshotArn")
    """
    The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
    """
    db_cluster_snapshot_identifier: pulumi.Output[str] = pulumi.output_property("dbClusterSnapshotIdentifier")
    """
    The Identifier for the snapshot.
    """
    engine: pulumi.Output[str] = pulumi.output_property("engine")
    """
    Specifies the name of the database engine.
    """
    engine_version: pulumi.Output[str] = pulumi.output_property("engineVersion")
    """
    Version of the database engine for this DB cluster snapshot.
    """
    kms_key_id: pulumi.Output[str] = pulumi.output_property("kmsKeyId")
    """
    If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
    """
    license_model: pulumi.Output[str] = pulumi.output_property("licenseModel")
    """
    License model information for the restored DB cluster.
    """
    port: pulumi.Output[float] = pulumi.output_property("port")
    """
    Port that the DB cluster was listening on at the time of the snapshot.
    """
    snapshot_type: pulumi.Output[str] = pulumi.output_property("snapshotType")
    source_db_cluster_snapshot_arn: pulumi.Output[str] = pulumi.output_property("sourceDbClusterSnapshotArn")
    status: pulumi.Output[str] = pulumi.output_property("status")
    """
    The status of this DB Cluster Snapshot.
    """
    storage_encrypted: pulumi.Output[bool] = pulumi.output_property("storageEncrypted")
    """
    Specifies whether the DB cluster snapshot is encrypted.
    """
    tags: pulumi.Output[Optional[Dict[str, str]]] = pulumi.output_property("tags")
    """
    A map of tags to assign to the DB cluster.
    """
    vpc_id: pulumi.Output[str] = pulumi.output_property("vpcId")
    """
    The VPC ID associated with the DB cluster snapshot.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, db_cluster_identifier: Optional[pulumi.Input[str]] = None, db_cluster_snapshot_identifier: Optional[pulumi.Input[str]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages an RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the `rds.Snapshot` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.rds.ClusterSnapshot("example",
            db_cluster_identifier=aws_rds_cluster["example"]["id"],
            db_cluster_snapshot_identifier="resourcetestsnapshot1234")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_cluster_identifier: The DB Cluster Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the DB cluster.
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

            if db_cluster_identifier is None:
                raise TypeError("Missing required property 'db_cluster_identifier'")
            __props__['db_cluster_identifier'] = db_cluster_identifier
            if db_cluster_snapshot_identifier is None:
                raise TypeError("Missing required property 'db_cluster_snapshot_identifier'")
            __props__['db_cluster_snapshot_identifier'] = db_cluster_snapshot_identifier
            __props__['tags'] = tags
            __props__['allocated_storage'] = None
            __props__['availability_zones'] = None
            __props__['db_cluster_snapshot_arn'] = None
            __props__['engine'] = None
            __props__['engine_version'] = None
            __props__['kms_key_id'] = None
            __props__['license_model'] = None
            __props__['port'] = None
            __props__['snapshot_type'] = None
            __props__['source_db_cluster_snapshot_arn'] = None
            __props__['status'] = None
            __props__['storage_encrypted'] = None
            __props__['vpc_id'] = None
        super(ClusterSnapshot, __self__).__init__(
            'aws:rds/clusterSnapshot:ClusterSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, allocated_storage: Optional[pulumi.Input[float]] = None, availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None, db_cluster_identifier: Optional[pulumi.Input[str]] = None, db_cluster_snapshot_arn: Optional[pulumi.Input[str]] = None, db_cluster_snapshot_identifier: Optional[pulumi.Input[str]] = None, engine: Optional[pulumi.Input[str]] = None, engine_version: Optional[pulumi.Input[str]] = None, kms_key_id: Optional[pulumi.Input[str]] = None, license_model: Optional[pulumi.Input[str]] = None, port: Optional[pulumi.Input[float]] = None, snapshot_type: Optional[pulumi.Input[str]] = None, source_db_cluster_snapshot_arn: Optional[pulumi.Input[str]] = None, status: Optional[pulumi.Input[str]] = None, storage_encrypted: Optional[pulumi.Input[bool]] = None, tags: Optional[pulumi.Input[Dict[str, pulumi.Input[str]]]] = None, vpc_id: Optional[pulumi.Input[str]] = None) -> 'ClusterSnapshot':
        """
        Get an existing ClusterSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allocated_storage: Specifies the allocated storage size in gigabytes (GB).
        :param pulumi.Input[List[pulumi.Input[str]]] availability_zones: List of EC2 Availability Zones that instances in the DB cluster snapshot can be restored in.
        :param pulumi.Input[str] db_cluster_identifier: The DB Cluster Identifier from which to take the snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_arn: The Amazon Resource Name (ARN) for the DB Cluster Snapshot.
        :param pulumi.Input[str] db_cluster_snapshot_identifier: The Identifier for the snapshot.
        :param pulumi.Input[str] engine: Specifies the name of the database engine.
        :param pulumi.Input[str] engine_version: Version of the database engine for this DB cluster snapshot.
        :param pulumi.Input[str] kms_key_id: If storage_encrypted is true, the AWS KMS key identifier for the encrypted DB cluster snapshot.
        :param pulumi.Input[str] license_model: License model information for the restored DB cluster.
        :param pulumi.Input[float] port: Port that the DB cluster was listening on at the time of the snapshot.
        :param pulumi.Input[str] status: The status of this DB Cluster Snapshot.
        :param pulumi.Input[bool] storage_encrypted: Specifies whether the DB cluster snapshot is encrypted.
        :param pulumi.Input[Dict[str, pulumi.Input[str]]] tags: A map of tags to assign to the DB cluster.
        :param pulumi.Input[str] vpc_id: The VPC ID associated with the DB cluster snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allocated_storage"] = allocated_storage
        __props__["availability_zones"] = availability_zones
        __props__["db_cluster_identifier"] = db_cluster_identifier
        __props__["db_cluster_snapshot_arn"] = db_cluster_snapshot_arn
        __props__["db_cluster_snapshot_identifier"] = db_cluster_snapshot_identifier
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["kms_key_id"] = kms_key_id
        __props__["license_model"] = license_model
        __props__["port"] = port
        __props__["snapshot_type"] = snapshot_type
        __props__["source_db_cluster_snapshot_arn"] = source_db_cluster_snapshot_arn
        __props__["status"] = status
        __props__["storage_encrypted"] = storage_encrypted
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return ClusterSnapshot(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

