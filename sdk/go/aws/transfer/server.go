// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package transfer

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a AWS Transfer Server resource.
type Server struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of Transfer Server
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
	// The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
	EndpointDetails ServerEndpointDetailsPtrOutput `pulumi:"endpointDetails"`
	// The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
	EndpointType pulumi.StringPtrOutput `pulumi:"endpointType"`
	// A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
	ForceDestroy pulumi.BoolPtrOutput `pulumi:"forceDestroy"`
	// RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
	HostKey pulumi.StringPtrOutput `pulumi:"hostKey"`
	// This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
	HostKeyFingerprint pulumi.StringOutput `pulumi:"hostKeyFingerprint"`
	// The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
	IdentityProviderType pulumi.StringPtrOutput `pulumi:"identityProviderType"`
	// Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
	InvocationRole pulumi.StringPtrOutput `pulumi:"invocationRole"`
	// Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
	LoggingRole pulumi.StringPtrOutput `pulumi:"loggingRole"`
	// A map of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
	Url pulumi.StringPtrOutput `pulumi:"url"`
}

// NewServer registers a new resource with the given unique name, arguments, and options.
func NewServer(ctx *pulumi.Context,
	name string, args *ServerArgs, opts ...pulumi.ResourceOption) (*Server, error) {
	if args == nil {
		args = &ServerArgs{}
	}
	var resource Server
	err := ctx.RegisterResource("aws:transfer/server:Server", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServer gets an existing Server resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerState, opts ...pulumi.ResourceOption) (*Server, error) {
	var resource Server
	err := ctx.ReadResource("aws:transfer/server:Server", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Server resources.
type serverState struct {
	// Amazon Resource Name (ARN) of Transfer Server
	Arn *string `pulumi:"arn"`
	// The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
	Endpoint *string `pulumi:"endpoint"`
	// The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
	EndpointDetails *ServerEndpointDetails `pulumi:"endpointDetails"`
	// The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
	EndpointType *string `pulumi:"endpointType"`
	// A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
	HostKey *string `pulumi:"hostKey"`
	// This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
	HostKeyFingerprint *string `pulumi:"hostKeyFingerprint"`
	// The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
	IdentityProviderType *string `pulumi:"identityProviderType"`
	// Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
	InvocationRole *string `pulumi:"invocationRole"`
	// Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
	LoggingRole *string `pulumi:"loggingRole"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
	Url *string `pulumi:"url"`
}

type ServerState struct {
	// Amazon Resource Name (ARN) of Transfer Server
	Arn pulumi.StringPtrInput
	// The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
	Endpoint pulumi.StringPtrInput
	// The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
	EndpointDetails ServerEndpointDetailsPtrInput
	// The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
	EndpointType pulumi.StringPtrInput
	// A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
	ForceDestroy pulumi.BoolPtrInput
	// RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
	HostKey pulumi.StringPtrInput
	// This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
	HostKeyFingerprint pulumi.StringPtrInput
	// The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
	IdentityProviderType pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
	InvocationRole pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
	LoggingRole pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
	Url pulumi.StringPtrInput
}

func (ServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverState)(nil)).Elem()
}

type serverArgs struct {
	// The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
	EndpointDetails *ServerEndpointDetails `pulumi:"endpointDetails"`
	// The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
	EndpointType *string `pulumi:"endpointType"`
	// A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
	HostKey *string `pulumi:"hostKey"`
	// The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
	IdentityProviderType *string `pulumi:"identityProviderType"`
	// Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
	InvocationRole *string `pulumi:"invocationRole"`
	// Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
	LoggingRole *string `pulumi:"loggingRole"`
	// A map of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
	// - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
	Url *string `pulumi:"url"`
}

// The set of arguments for constructing a Server resource.
type ServerArgs struct {
	// The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
	EndpointDetails ServerEndpointDetailsPtrInput
	// The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
	EndpointType pulumi.StringPtrInput
	// A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
	ForceDestroy pulumi.BoolPtrInput
	// RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
	HostKey pulumi.StringPtrInput
	// The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
	IdentityProviderType pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
	InvocationRole pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
	LoggingRole pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.MapInput
	// - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
	Url pulumi.StringPtrInput
}

func (ServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverArgs)(nil)).Elem()
}
