// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a AWS Transfer Server resource.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const fooRole = new aws.iam.Role("fooRole", {assumeRolePolicy: `{
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 		"Effect": "Allow",
 * 		"Principal": {
 * 			"Service": "transfer.amazonaws.com"
 * 		},
 * 		"Action": "sts:AssumeRole"
 * 		}
 * 	]
 * }
 * `});
 * const fooRolePolicy = new aws.iam.RolePolicy("fooRolePolicy", {
 *     role: fooRole.id,
 *     policy: `{
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 		"Sid": "AllowFullAccesstoCloudWatchLogs",
 * 		"Effect": "Allow",
 * 		"Action": [
 * 			"logs:*"
 * 		],
 * 		"Resource": "*"
 * 		}
 * 	]
 * }
 * `,
 * });
 * const fooServer = new aws.transfer.Server("fooServer", {
 *     identityProviderType: "SERVICE_MANAGED",
 *     loggingRole: fooRole.arn,
 *     tags: {
 *         NAME: "tf-acc-test-transfer-server",
 *         ENV: "test",
 *     },
 * });
 * ```
 */
export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:transfer/server:Server';

    /**
     * Returns true if the given object is an instance of Server.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Server {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Server.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of Transfer Server
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
     */
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    /**
     * The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
     */
    public readonly endpointDetails!: pulumi.Output<outputs.transfer.ServerEndpointDetails | undefined>;
    /**
     * The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
     */
    public readonly endpointType!: pulumi.Output<string | undefined>;
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    public readonly forceDestroy!: pulumi.Output<boolean | undefined>;
    /**
     * RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
     */
    public readonly hostKey!: pulumi.Output<string | undefined>;
    /**
     * This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
     */
    public /*out*/ readonly hostKeyFingerprint!: pulumi.Output<string>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    public readonly identityProviderType!: pulumi.Output<string | undefined>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
     */
    public readonly invocationRole!: pulumi.Output<string | undefined>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    public readonly loggingRole!: pulumi.Output<string | undefined>;
    /**
     * A map of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
     */
    public readonly url!: pulumi.Output<string | undefined>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerArgs | ServerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ServerState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["endpoint"] = state ? state.endpoint : undefined;
            inputs["endpointDetails"] = state ? state.endpointDetails : undefined;
            inputs["endpointType"] = state ? state.endpointType : undefined;
            inputs["forceDestroy"] = state ? state.forceDestroy : undefined;
            inputs["hostKey"] = state ? state.hostKey : undefined;
            inputs["hostKeyFingerprint"] = state ? state.hostKeyFingerprint : undefined;
            inputs["identityProviderType"] = state ? state.identityProviderType : undefined;
            inputs["invocationRole"] = state ? state.invocationRole : undefined;
            inputs["loggingRole"] = state ? state.loggingRole : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as ServerArgs | undefined;
            inputs["endpointDetails"] = args ? args.endpointDetails : undefined;
            inputs["endpointType"] = args ? args.endpointType : undefined;
            inputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            inputs["hostKey"] = args ? args.hostKey : undefined;
            inputs["identityProviderType"] = args ? args.identityProviderType : undefined;
            inputs["invocationRole"] = args ? args.invocationRole : undefined;
            inputs["loggingRole"] = args ? args.loggingRole : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["url"] = args ? args.url : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["endpoint"] = undefined /*out*/;
            inputs["hostKeyFingerprint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Server.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Server resources.
 */
export interface ServerState {
    /**
     * Amazon Resource Name (ARN) of Transfer Server
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
     */
    readonly endpoint?: pulumi.Input<string>;
    /**
     * The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
     */
    readonly endpointDetails?: pulumi.Input<inputs.transfer.ServerEndpointDetails>;
    /**
     * The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
     */
    readonly endpointType?: pulumi.Input<string>;
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
     */
    readonly hostKey?: pulumi.Input<string>;
    /**
     * This value contains the message-digest algorithm (MD5) hash of the server's host key. This value is equivalent to the output of the `ssh-keygen -l -E md5 -f my-new-server-key` command.
     */
    readonly hostKeyFingerprint?: pulumi.Input<string>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    readonly identityProviderType?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
     */
    readonly invocationRole?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    readonly loggingRole?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    /**
     * The virtual private cloud (VPC) endpoint settings that you want to configure for your SFTP server. Fields documented below.
     */
    readonly endpointDetails?: pulumi.Input<inputs.transfer.ServerEndpointDetails>;
    /**
     * The type of endpoint that you want your SFTP server connect to. If you connect to a `VPC_ENDPOINT`, your SFTP server isn't accessible over the public internet. If you want to connect your SFTP server via public internet, set `PUBLIC`.  Defaults to `PUBLIC`.
     */
    readonly endpointType?: pulumi.Input<string>;
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * RSA private key (e.g. as generated by the `ssh-keygen -N "" -f my-new-server-key` command).
     */
    readonly hostKey?: pulumi.Input<string>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    readonly identityProviderType?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identityProviderType` of `API_GATEWAY`.
     */
    readonly invocationRole?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    readonly loggingRole?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identityProviderType` of `API_GATEWAY`.
     */
    readonly url?: pulumi.Input<string>;
}
