# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'WindowsFileSystemSelfManagedActiveDirectoryArgs',
]

@pulumi.input_type
class WindowsFileSystemSelfManagedActiveDirectoryArgs:
    dns_ips: pulumi.Input[List[pulumi.Input[str]]] = pulumi.input_property("dnsIps")
    """
    A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
    """
    domain_name: pulumi.Input[str] = pulumi.input_property("domainName")
    """
    The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
    """
    password: pulumi.Input[str] = pulumi.input_property("password")
    """
    The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
    """
    username: pulumi.Input[str] = pulumi.input_property("username")
    """
    The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
    """
    file_system_administrators_group: Optional[pulumi.Input[str]] = pulumi.input_property("fileSystemAdministratorsGroup")
    """
    The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
    """
    organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = pulumi.input_property("organizationalUnitDistinguishedName")
    """
    The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
    """

    # pylint: disable=no-self-argument
    def __init__(__self__, *, dns_ips: pulumi.Input[List[pulumi.Input[str]]], domain_name: pulumi.Input[str], password: pulumi.Input[str], username: pulumi.Input[str], file_system_administrators_group: Optional[pulumi.Input[str]] = None, organizational_unit_distinguished_name: Optional[pulumi.Input[str]] = None) -> None:
        """
        :param pulumi.Input[List[pulumi.Input[str]]] dns_ips: A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
        :param pulumi.Input[str] domain_name: The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
        :param pulumi.Input[str] password: The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        :param pulumi.Input[str] username: The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
        :param pulumi.Input[str] file_system_administrators_group: The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
        :param pulumi.Input[str] organizational_unit_distinguished_name: The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
        """
        __self__.dns_ips = dns_ips
        __self__.domain_name = domain_name
        __self__.password = password
        __self__.username = username
        __self__.file_system_administrators_group = file_system_administrators_group
        __self__.organizational_unit_distinguished_name = organizational_unit_distinguished_name

