# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class VirtualNode(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the virtual node.
    """
    created_date: pulumi.Output[str]
    """
    The creation date of the virtual node.
    """
    last_updated_date: pulumi.Output[str]
    """
    The last update date of the virtual node.
    """
    mesh_name: pulumi.Output[str]
    """
    The name of the service mesh in which to create the virtual node.
    """
    name: pulumi.Output[str]
    """
    The name to use for the virtual node.
    """
    spec: pulumi.Output[dict]
    """
    The virtual node specification to apply.

      * `backends` (`list`) - The backends to which the virtual node is expected to send outbound traffic.
        * `virtualService` (`dict`) - Specifies a virtual service to use as a backend for a virtual node.
          * `virtualServiceName` (`str`) - The name of the virtual service that is acting as a virtual node backend.

      * `listener` (`dict`) - The listeners from which the virtual node is expected to receive inbound traffic.
        * `health_check` (`dict`) - The health check information for the listener.
          * `healthyThreshold` (`float`) - The number of consecutive successful health checks that must occur before declaring listener healthy.
          * `intervalMillis` (`float`) - The time period in milliseconds between each health check execution.
          * `path` (`str`) - The destination path for the health check request. This is only required if the specified protocol is `http`.
          * `port` (`float`) - The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
          * `protocol` (`str`) - The protocol for the health check request. Valid values are `http` and `tcp`.
          * `timeoutMillis` (`float`) - The amount of time to wait when receiving a response from the health check, in milliseconds.
          * `unhealthyThreshold` (`float`) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.

        * `portMapping` (`dict`) - The port mapping information for the listener.
          * `port` (`float`) - The port used for the port mapping.
          * `protocol` (`str`) - The protocol used for the port mapping. Valid values are `http` and `tcp`.

      * `logging` (`dict`) - The inbound and outbound access logging information for the virtual node.
        * `accessLog` (`dict`) - The access log configuration for a virtual node.
          * `file` (`dict`) - The file object to send virtual node access logs to.
            * `path` (`str`) - The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out.

      * `serviceDiscovery` (`dict`) - The service discovery information for the virtual node.
        * `awsCloudMap` (`dict`) - Specifies any AWS Cloud Map information for the virtual node.
          * `attributes` (`dict`) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
          * `namespaceName` (`str`) - The name of the AWS Cloud Map namespace to use.
            Use the [`servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
          * `service_name` (`str`) - The name of the AWS Cloud Map service to use. Use the [`servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.

        * `dns` (`dict`) - Specifies the DNS service name for the virtual node.
          * `hostname` (`str`) - The DNS host name for your virtual node.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, mesh_name=None, name=None, spec=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an AWS App Mesh virtual node resource.

        ## Breaking Changes

        Because of backward incompatible API changes (read [here](https://github.com/awslabs/aws-app-mesh-examples/issues/92)), `appmesh.VirtualNode` resource definitions created with provider versions earlier than v2.3.0 will need to be modified:

        * Rename the `service_name` attribute of the `dns` object to `hostname`.

        * Replace the `backends` attribute of the `spec` object with one or more `backend` configuration blocks,
        setting `virtual_service_name` to the name of the service.

        The state associated with existing resources will automatically be migrated.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the virtual node.
        :param pulumi.Input[str] name: The name to use for the virtual node.
        :param pulumi.Input[dict] spec: The virtual node specification to apply.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.

        The **spec** object supports the following:

          * `backends` (`pulumi.Input[list]`) - The backends to which the virtual node is expected to send outbound traffic.
            * `virtualService` (`pulumi.Input[dict]`) - Specifies a virtual service to use as a backend for a virtual node.
              * `virtualServiceName` (`pulumi.Input[str]`) - The name of the virtual service that is acting as a virtual node backend.

          * `listener` (`pulumi.Input[dict]`) - The listeners from which the virtual node is expected to receive inbound traffic.
            * `health_check` (`pulumi.Input[dict]`) - The health check information for the listener.
              * `healthyThreshold` (`pulumi.Input[float]`) - The number of consecutive successful health checks that must occur before declaring listener healthy.
              * `intervalMillis` (`pulumi.Input[float]`) - The time period in milliseconds between each health check execution.
              * `path` (`pulumi.Input[str]`) - The destination path for the health check request. This is only required if the specified protocol is `http`.
              * `port` (`pulumi.Input[float]`) - The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
              * `protocol` (`pulumi.Input[str]`) - The protocol for the health check request. Valid values are `http` and `tcp`.
              * `timeoutMillis` (`pulumi.Input[float]`) - The amount of time to wait when receiving a response from the health check, in milliseconds.
              * `unhealthyThreshold` (`pulumi.Input[float]`) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.

            * `portMapping` (`pulumi.Input[dict]`) - The port mapping information for the listener.
              * `port` (`pulumi.Input[float]`) - The port used for the port mapping.
              * `protocol` (`pulumi.Input[str]`) - The protocol used for the port mapping. Valid values are `http` and `tcp`.

          * `logging` (`pulumi.Input[dict]`) - The inbound and outbound access logging information for the virtual node.
            * `accessLog` (`pulumi.Input[dict]`) - The access log configuration for a virtual node.
              * `file` (`pulumi.Input[dict]`) - The file object to send virtual node access logs to.
                * `path` (`pulumi.Input[str]`) - The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out.

          * `serviceDiscovery` (`pulumi.Input[dict]`) - The service discovery information for the virtual node.
            * `awsCloudMap` (`pulumi.Input[dict]`) - Specifies any AWS Cloud Map information for the virtual node.
              * `attributes` (`pulumi.Input[dict]`) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
              * `namespaceName` (`pulumi.Input[str]`) - The name of the AWS Cloud Map namespace to use.
                Use the [`servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
              * `service_name` (`pulumi.Input[str]`) - The name of the AWS Cloud Map service to use. Use the [`servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.

            * `dns` (`pulumi.Input[dict]`) - Specifies the DNS service name for the virtual node.
              * `hostname` (`pulumi.Input[str]`) - The DNS host name for your virtual node.
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

            if mesh_name is None:
                raise TypeError("Missing required property 'mesh_name'")
            __props__['mesh_name'] = mesh_name
            __props__['name'] = name
            if spec is None:
                raise TypeError("Missing required property 'spec'")
            __props__['spec'] = spec
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['created_date'] = None
            __props__['last_updated_date'] = None
        super(VirtualNode, __self__).__init__(
            'aws:appmesh/virtualNode:VirtualNode',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, created_date=None, last_updated_date=None, mesh_name=None, name=None, spec=None, tags=None):
        """
        Get an existing VirtualNode resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the virtual node.
        :param pulumi.Input[str] created_date: The creation date of the virtual node.
        :param pulumi.Input[str] last_updated_date: The last update date of the virtual node.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the virtual node.
        :param pulumi.Input[str] name: The name to use for the virtual node.
        :param pulumi.Input[dict] spec: The virtual node specification to apply.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.

        The **spec** object supports the following:

          * `backends` (`pulumi.Input[list]`) - The backends to which the virtual node is expected to send outbound traffic.
            * `virtualService` (`pulumi.Input[dict]`) - Specifies a virtual service to use as a backend for a virtual node.
              * `virtualServiceName` (`pulumi.Input[str]`) - The name of the virtual service that is acting as a virtual node backend.

          * `listener` (`pulumi.Input[dict]`) - The listeners from which the virtual node is expected to receive inbound traffic.
            * `health_check` (`pulumi.Input[dict]`) - The health check information for the listener.
              * `healthyThreshold` (`pulumi.Input[float]`) - The number of consecutive successful health checks that must occur before declaring listener healthy.
              * `intervalMillis` (`pulumi.Input[float]`) - The time period in milliseconds between each health check execution.
              * `path` (`pulumi.Input[str]`) - The destination path for the health check request. This is only required if the specified protocol is `http`.
              * `port` (`pulumi.Input[float]`) - The destination port for the health check request. This port must match the port defined in the `port_mapping` for the listener.
              * `protocol` (`pulumi.Input[str]`) - The protocol for the health check request. Valid values are `http` and `tcp`.
              * `timeoutMillis` (`pulumi.Input[float]`) - The amount of time to wait when receiving a response from the health check, in milliseconds.
              * `unhealthyThreshold` (`pulumi.Input[float]`) - The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.

            * `portMapping` (`pulumi.Input[dict]`) - The port mapping information for the listener.
              * `port` (`pulumi.Input[float]`) - The port used for the port mapping.
              * `protocol` (`pulumi.Input[str]`) - The protocol used for the port mapping. Valid values are `http` and `tcp`.

          * `logging` (`pulumi.Input[dict]`) - The inbound and outbound access logging information for the virtual node.
            * `accessLog` (`pulumi.Input[dict]`) - The access log configuration for a virtual node.
              * `file` (`pulumi.Input[dict]`) - The file object to send virtual node access logs to.
                * `path` (`pulumi.Input[str]`) - The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out.

          * `serviceDiscovery` (`pulumi.Input[dict]`) - The service discovery information for the virtual node.
            * `awsCloudMap` (`pulumi.Input[dict]`) - Specifies any AWS Cloud Map information for the virtual node.
              * `attributes` (`pulumi.Input[dict]`) - A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.
              * `namespaceName` (`pulumi.Input[str]`) - The name of the AWS Cloud Map namespace to use.
                Use the [`servicediscovery.HttpNamespace`](https://www.terraform.io/docs/providers/aws/r/service_discovery_http_namespace.html) resource to configure a Cloud Map namespace.
              * `service_name` (`pulumi.Input[str]`) - The name of the AWS Cloud Map service to use. Use the [`servicediscovery.Service`](https://www.terraform.io/docs/providers/aws/r/service_discovery_service.html) resource to configure a Cloud Map service.

            * `dns` (`pulumi.Input[dict]`) - Specifies the DNS service name for the virtual node.
              * `hostname` (`pulumi.Input[str]`) - The DNS host name for your virtual node.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["created_date"] = created_date
        __props__["last_updated_date"] = last_updated_date
        __props__["mesh_name"] = mesh_name
        __props__["name"] = name
        __props__["spec"] = spec
        __props__["tags"] = tags
        return VirtualNode(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

