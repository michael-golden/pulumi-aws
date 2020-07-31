# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class BasePathMapping(pulumi.CustomResource):
    base_path: pulumi.Output[str]
    """
    Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
    """
    domain_name: pulumi.Output[str]
    """
    The already-registered domain name to connect the API to.
    """
    rest_api: pulumi.Output[str]
    """
    The id of the API to connect.
    """
    stage_name: pulumi.Output[str]
    """
    The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
    """
    def __init__(__self__, resource_name, opts=None, base_path=None, domain_name=None, rest_api=None, stage_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Connects a custom domain name registered via `apigateway.DomainName`
        with a deployed API so that its methods can be called via the
        custom domain name.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_deployment = aws.apigateway.Deployment("exampleDeployment",
            rest_api=aws_api_gateway_rest_api["MyDemoAPI"]["id"],
            stage_name="live")
        example_domain_name = aws.apigateway.DomainName("exampleDomainName",
            domain_name="example.com",
            certificate_name="example-api",
            certificate_body=(lambda path: open(path).read())(f"{path['module']}/example.com/example.crt"),
            certificate_chain=(lambda path: open(path).read())(f"{path['module']}/example.com/ca.crt"),
            certificate_private_key=(lambda path: open(path).read())(f"{path['module']}/example.com/example.key"))
        test = aws.apigateway.BasePathMapping("test",
            rest_api=aws_api_gateway_rest_api["MyDemoAPI"]["id"],
            stage_name=example_deployment.stage_name,
            domain_name=example_domain_name.domain_name)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_path: Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
        :param pulumi.Input[str] domain_name: The already-registered domain name to connect the API to.
        :param pulumi.Input[dict] rest_api: The id of the API to connect.
        :param pulumi.Input[str] stage_name: The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
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

            __props__['base_path'] = base_path
            if domain_name is None:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            if rest_api is None:
                raise TypeError("Missing required property 'rest_api'")
            __props__['rest_api'] = rest_api
            __props__['stage_name'] = stage_name
        super(BasePathMapping, __self__).__init__(
            'aws:apigateway/basePathMapping:BasePathMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, base_path=None, domain_name=None, rest_api=None, stage_name=None):
        """
        Get an existing BasePathMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_path: Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
        :param pulumi.Input[str] domain_name: The already-registered domain name to connect the API to.
        :param pulumi.Input[dict] rest_api: The id of the API to connect.
        :param pulumi.Input[str] stage_name: The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["base_path"] = base_path
        __props__["domain_name"] = domain_name
        __props__["rest_api"] = rest_api
        __props__["stage_name"] = stage_name
        return BasePathMapping(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
