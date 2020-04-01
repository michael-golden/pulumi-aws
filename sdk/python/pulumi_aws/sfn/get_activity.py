# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetActivityResult:
    """
    A collection of values returned by getActivity.
    """
    def __init__(__self__, arn=None, creation_date=None, id=None, name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        __self__.creation_date = creation_date
        """
        The date the activity was created.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
class AwaitableGetActivityResult(GetActivityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActivityResult(
            arn=self.arn,
            creation_date=self.creation_date,
            id=self.id,
            name=self.name)

def get_activity(arn=None,name=None,opts=None):
    """
    Provides a Step Functions Activity data source



    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sfn_activity.html.markdown.


    :param str arn: The Amazon Resource Name (ARN) that identifies the activity.
    :param str name: The name that identifies the activity.
    """
    __args__ = dict()


    __args__['arn'] = arn
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:sfn/getActivity:getActivity', __args__, opts=opts).value

    return AwaitableGetActivityResult(
        arn=__ret__.get('arn'),
        creation_date=__ret__.get('creationDate'),
        id=__ret__.get('id'),
        name=__ret__.get('name'))
