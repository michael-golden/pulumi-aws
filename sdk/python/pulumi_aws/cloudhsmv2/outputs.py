# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterClusterCertificate',
    'GetClusterClusterCertificates',
]

@pulumi.output_type
class ClusterClusterCertificate(dict):
    aws_hardware_certificate: Optional[str] = pulumi.output_property("awsHardwareCertificate")
    cluster_certificate: Optional[str] = pulumi.output_property("clusterCertificate")
    cluster_csr: Optional[str] = pulumi.output_property("clusterCsr")
    hsm_certificate: Optional[str] = pulumi.output_property("hsmCertificate")
    manufacturer_hardware_certificate: Optional[str] = pulumi.output_property("manufacturerHardwareCertificate")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetClusterClusterCertificates(dict):
    aws_hardware_certificate: str = pulumi.output_property("awsHardwareCertificate")
    cluster_certificate: str = pulumi.output_property("clusterCertificate")
    cluster_csr: str = pulumi.output_property("clusterCsr")
    hsm_certificate: str = pulumi.output_property("hsmCertificate")
    manufacturer_hardware_certificate: str = pulumi.output_property("manufacturerHardwareCertificate")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


