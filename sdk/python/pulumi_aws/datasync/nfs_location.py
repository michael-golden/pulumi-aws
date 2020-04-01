# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class NfsLocation(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the DataSync Location.
    """
    on_prem_config: pulumi.Output[dict]
    """
    Configuration block containing information for connecting to the NFS File System.

      * `agent_arns` (`list`) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.
    """
    server_hostname: pulumi.Output[str]
    """
    Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.
    """
    subdirectory: pulumi.Output[str]
    """
    Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
    """
    tags: pulumi.Output[dict]
    """
    Key-value pairs of resource tags to assign to the DataSync Location.
    """
    uri: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, on_prem_config=None, server_hostname=None, subdirectory=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an NFS Location within AWS DataSync.

        > **NOTE:** The DataSync Agents must be available before creating this resource.



        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_location_nfs.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] on_prem_config: Configuration block containing information for connecting to the NFS File System.
        :param pulumi.Input[str] server_hostname: Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.
        :param pulumi.Input[str] subdirectory: Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Location.

        The **on_prem_config** object supports the following:

          * `agent_arns` (`pulumi.Input[list]`) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if on_prem_config is None:
                raise TypeError("Missing required property 'on_prem_config'")
            __props__['on_prem_config'] = on_prem_config
            if server_hostname is None:
                raise TypeError("Missing required property 'server_hostname'")
            __props__['server_hostname'] = server_hostname
            if subdirectory is None:
                raise TypeError("Missing required property 'subdirectory'")
            __props__['subdirectory'] = subdirectory
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['uri'] = None
        super(NfsLocation, __self__).__init__(
            'aws:datasync/nfsLocation:NfsLocation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, on_prem_config=None, server_hostname=None, subdirectory=None, tags=None, uri=None):
        """
        Get an existing NfsLocation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the DataSync Location.
        :param pulumi.Input[dict] on_prem_config: Configuration block containing information for connecting to the NFS File System.
        :param pulumi.Input[str] server_hostname: Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.
        :param pulumi.Input[str] subdirectory: Subdirectory to perform actions as source or destination. Should be exported by the NFS server.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Location.

        The **on_prem_config** object supports the following:

          * `agent_arns` (`pulumi.Input[list]`) - List of Amazon Resource Names (ARNs) of the DataSync Agents used to connect to the NFS server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["on_prem_config"] = on_prem_config
        __props__["server_hostname"] = server_hostname
        __props__["subdirectory"] = subdirectory
        __props__["tags"] = tags
        __props__["uri"] = uri
        return NfsLocation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

