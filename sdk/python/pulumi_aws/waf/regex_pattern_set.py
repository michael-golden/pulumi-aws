# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RegexPatternSet(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    The name or description of the Regex Pattern Set.
    """
    regex_pattern_strings: pulumi.Output[list]
    """
    A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, regex_pattern_strings=None):
        """
        Provides a WAF Regex Pattern Set Resource
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] name: The name or description of the Regex Pattern Set.
        :param pulumi.Input[list] regex_pattern_strings: A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        __props__['regex_pattern_strings'] = regex_pattern_strings

        super(RegexPatternSet, __self__).__init__(
            'aws:waf/regexPatternSet:RegexPatternSet',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

