# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Model']


class Model(pulumi.CustomResource):
    api_id: pulumi.Output[str] = pulumi.output_property("apiId")
    """
    The API identifier.
    """
    content_type: pulumi.Output[str] = pulumi.output_property("contentType")
    """
    The content-type for the model, for example, `application/json`.
    """
    description: pulumi.Output[Optional[str]] = pulumi.output_property("description")
    """
    The description of the model.
    """
    name: pulumi.Output[str] = pulumi.output_property("name")
    """
    The name of the model. Must be alphanumeric.
    """
    schema: pulumi.Output[str] = pulumi.output_property("schema")
    """
    The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
    """
    # pylint: disable=no-self-argument
    def __init__(__self__, resource_name, opts: Optional[pulumi.ResourceOptions] = None, api_id: Optional[pulumi.Input[str]] = None, content_type: Optional[pulumi.Input[str]] = None, description: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, schema: Optional[pulumi.Input[str]] = None, __props__=None, __name__=None, __opts__=None) -> None:
        """
        Manages an Amazon API Gateway Version 2 [model](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-models).

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Model("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            content_type="application/json",
            schema=\"\"\"{
          "$schema": "http://json-schema.org/draft-04/schema#",
          "title": "ExampleModel",
          "type": "object",
          "properties": {
            "id": { "type": "string" }
          }
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] content_type: The content-type for the model, for example, `application/json`.
        :param pulumi.Input[str] description: The description of the model.
        :param pulumi.Input[str] name: The name of the model. Must be alphanumeric.
        :param pulumi.Input[str] schema: The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
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

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            if content_type is None:
                raise TypeError("Missing required property 'content_type'")
            __props__['content_type'] = content_type
            __props__['description'] = description
            __props__['name'] = name
            if schema is None:
                raise TypeError("Missing required property 'schema'")
            __props__['schema'] = schema
        super(Model, __self__).__init__(
            'aws:apigatewayv2/model:Model',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str, id: str, opts: Optional[pulumi.ResourceOptions] = None, api_id: Optional[pulumi.Input[str]] = None, content_type: Optional[pulumi.Input[str]] = None, description: Optional[pulumi.Input[str]] = None, name: Optional[pulumi.Input[str]] = None, schema: Optional[pulumi.Input[str]] = None) -> 'Model':
        """
        Get an existing Model resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] content_type: The content-type for the model, for example, `application/json`.
        :param pulumi.Input[str] description: The description of the model.
        :param pulumi.Input[str] name: The name of the model. Must be alphanumeric.
        :param pulumi.Input[str] schema: The schema for the model. This should be a [JSON schema draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04) model.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["content_type"] = content_type
        __props__["description"] = description
        __props__["name"] = name
        __props__["schema"] = schema
        return Model(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

