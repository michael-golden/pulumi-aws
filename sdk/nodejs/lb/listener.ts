// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a Load Balancer Listener resource.
 *
 * > **Note:** `aws.alb.Listener` is known as `aws.lb.Listener`. The functionality is identical.
 *
 * ## Example Usage
 * ### Forward Action
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const frontEndLoadBalancer = new aws.lb.LoadBalancer("frontEndLoadBalancer", {});
 * // ...
 * const frontEndTargetGroup = new aws.lb.TargetGroup("frontEndTargetGroup", {});
 * // ...
 * const frontEndListener = new aws.lb.Listener("frontEndListener", {
 *     loadBalancerArn: frontEndLoadBalancer.arn,
 *     port: "443",
 *     protocol: "HTTPS",
 *     sslPolicy: "ELBSecurityPolicy-2016-08",
 *     certificateArn: "arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4",
 *     defaultActions: [{
 *         type: "forward",
 *         targetGroupArn: frontEndTargetGroup.arn,
 *     }],
 * });
 * ```
 * ### Redirect Action
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const frontEndLoadBalancer = new aws.lb.LoadBalancer("frontEndLoadBalancer", {});
 * // ...
 * const frontEndListener = new aws.lb.Listener("frontEndListener", {
 *     loadBalancerArn: frontEndLoadBalancer.arn,
 *     port: "80",
 *     protocol: "HTTP",
 *     defaultActions: [{
 *         type: "redirect",
 *         redirect: {
 *             port: "443",
 *             protocol: "HTTPS",
 *             statusCode: "HTTP_301",
 *         },
 *     }],
 * });
 * ```
 * ### Fixed-response Action
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const frontEndLoadBalancer = new aws.lb.LoadBalancer("frontEndLoadBalancer", {});
 * // ...
 * const frontEndListener = new aws.lb.Listener("frontEndListener", {
 *     loadBalancerArn: frontEndLoadBalancer.arn,
 *     port: "80",
 *     protocol: "HTTP",
 *     defaultActions: [{
 *         type: "fixed-response",
 *         fixedResponse: {
 *             contentType: "text/plain",
 *             messageBody: "Fixed response content",
 *             statusCode: "200",
 *         },
 *     }],
 * });
 * ```
 * ### Authenticate-cognito Action
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const frontEndLoadBalancer = new aws.lb.LoadBalancer("frontEndLoadBalancer", {});
 * // ...
 * const frontEndTargetGroup = new aws.lb.TargetGroup("frontEndTargetGroup", {});
 * // ...
 * const pool = new aws.cognito.UserPool("pool", {});
 * // ...
 * const client = new aws.cognito.UserPoolClient("client", {});
 * // ...
 * const domain = new aws.cognito.UserPoolDomain("domain", {});
 * // ...
 * const frontEndListener = new aws.lb.Listener("frontEndListener", {
 *     loadBalancerArn: frontEndLoadBalancer.arn,
 *     port: "80",
 *     protocol: "HTTP",
 *     defaultActions: [
 *         {
 *             type: "authenticate-cognito",
 *             authenticateCognito: {
 *                 userPoolArn: pool.arn,
 *                 userPoolClientId: client.id,
 *                 userPoolDomain: domain.domain,
 *             },
 *         },
 *         {
 *             type: "forward",
 *             targetGroupArn: frontEndTargetGroup.arn,
 *         },
 *     ],
 * });
 * ```
 * ### Authenticate-oidc Action
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const frontEndLoadBalancer = new aws.lb.LoadBalancer("frontEndLoadBalancer", {});
 * // ...
 * const frontEndTargetGroup = new aws.lb.TargetGroup("frontEndTargetGroup", {});
 * // ...
 * const frontEndListener = new aws.lb.Listener("frontEndListener", {
 *     loadBalancerArn: frontEndLoadBalancer.arn,
 *     port: "80",
 *     protocol: "HTTP",
 *     defaultActions: [
 *         {
 *             type: "authenticate-oidc",
 *             authenticateOidc: {
 *                 authorizationEndpoint: "https://example.com/authorization_endpoint",
 *                 clientId: "client_id",
 *                 clientSecret: "client_secret",
 *                 issuer: "https://example.com",
 *                 tokenEndpoint: "https://example.com/token_endpoint",
 *                 userInfoEndpoint: "https://example.com/user_info_endpoint",
 *             },
 *         },
 *         {
 *             type: "forward",
 *             targetGroupArn: frontEndTargetGroup.arn,
 *         },
 *     ],
 * });
 * ```
 */
export class Listener extends pulumi.CustomResource {
    /**
     * Get an existing Listener resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ListenerState, opts?: pulumi.CustomResourceOptions): Listener {
        return new Listener(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:lb/listener:Listener';

    /**
     * Returns true if the given object is an instance of Listener.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Listener {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Listener.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the target group.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `aws.lb.ListenerCertificate` resource.
     */
    public readonly certificateArn!: pulumi.Output<string | undefined>;
    /**
     * An Action block. Action blocks are documented below.
     */
    public readonly defaultActions!: pulumi.Output<outputs.lb.ListenerDefaultAction[]>;
    /**
     * The ARN of the load balancer.
     */
    public readonly loadBalancerArn!: pulumi.Output<string>;
    /**
     * The port on which the load balancer is listening.
     */
    public readonly port!: pulumi.Output<number>;
    /**
     * The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
     */
    public readonly protocol!: pulumi.Output<string | undefined>;
    /**
     * The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.
     */
    public readonly sslPolicy!: pulumi.Output<string>;

    /**
     * Create a Listener resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ListenerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ListenerArgs | ListenerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ListenerState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["certificateArn"] = state ? state.certificateArn : undefined;
            inputs["defaultActions"] = state ? state.defaultActions : undefined;
            inputs["loadBalancerArn"] = state ? state.loadBalancerArn : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["sslPolicy"] = state ? state.sslPolicy : undefined;
        } else {
            const args = argsOrState as ListenerArgs | undefined;
            if (!args || args.defaultActions === undefined) {
                throw new Error("Missing required property 'defaultActions'");
            }
            if (!args || args.loadBalancerArn === undefined) {
                throw new Error("Missing required property 'loadBalancerArn'");
            }
            if (!args || args.port === undefined) {
                throw new Error("Missing required property 'port'");
            }
            inputs["certificateArn"] = args ? args.certificateArn : undefined;
            inputs["defaultActions"] = args ? args.defaultActions : undefined;
            inputs["loadBalancerArn"] = args ? args.loadBalancerArn : undefined;
            inputs["port"] = args ? args.port : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["sslPolicy"] = args ? args.sslPolicy : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        const aliasOpts = { aliases: [{ type: "aws:elasticloadbalancingv2/listener:Listener" }] };
        opts = opts ? pulumi.mergeOptions(opts, aliasOpts) : aliasOpts;
        super(Listener.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Listener resources.
 */
export interface ListenerState {
    /**
     * The Amazon Resource Name (ARN) of the target group.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `aws.lb.ListenerCertificate` resource.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * An Action block. Action blocks are documented below.
     */
    readonly defaultActions?: pulumi.Input<pulumi.Input<inputs.lb.ListenerDefaultAction>[]>;
    /**
     * The ARN of the load balancer.
     */
    readonly loadBalancerArn?: pulumi.Input<string>;
    /**
     * The port on which the load balancer is listening.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.
     */
    readonly sslPolicy?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Listener resource.
 */
export interface ListenerArgs {
    /**
     * The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `aws.lb.ListenerCertificate` resource.
     */
    readonly certificateArn?: pulumi.Input<string>;
    /**
     * An Action block. Action blocks are documented below.
     */
    readonly defaultActions: pulumi.Input<pulumi.Input<inputs.lb.ListenerDefaultAction>[]>;
    /**
     * The ARN of the load balancer.
     */
    readonly loadBalancerArn: pulumi.Input<string>;
    /**
     * The port on which the load balancer is listening.
     */
    readonly port: pulumi.Input<number>;
    /**
     * The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.
     */
    readonly sslPolicy?: pulumi.Input<string>;
}
