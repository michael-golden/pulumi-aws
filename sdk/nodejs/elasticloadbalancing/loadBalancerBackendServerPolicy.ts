// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Attaches a load balancer policy to an ELB backend server.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * from "fs";
 *
 * const wu_tang = new aws.elb.LoadBalancer("wu-tang", {
 *     availabilityZones: ["us-east-1a"],
 *     listeners: [{
 *         instancePort: 443,
 *         instanceProtocol: "http",
 *         lbPort: 443,
 *         lbProtocol: "https",
 *         sslCertificateId: "arn:aws:iam::000000000000:server-certificate/wu-tang.net",
 *     }],
 *     tags: {
 *         Name: "wu-tang",
 *     },
 * });
 * const wu_tang_ca_pubkey_policy = new aws.elb.LoadBalancerPolicy("wu-tang-ca-pubkey-policy", {
 *     loadBalancerName: wu_tang.name,
 *     policyName: "wu-tang-ca-pubkey-policy",
 *     policyTypeName: "PublicKeyPolicyType",
 *     policyAttributes: [{
 *         name: "PublicKey",
 *         value: fs.readFileSync("wu-tang-pubkey"),
 *     }],
 * });
 * const wu_tang_root_ca_backend_auth_policy = new aws.elb.LoadBalancerPolicy("wu-tang-root-ca-backend-auth-policy", {
 *     loadBalancerName: wu_tang.name,
 *     policyName: "wu-tang-root-ca-backend-auth-policy",
 *     policyTypeName: "BackendServerAuthenticationPolicyType",
 *     policyAttributes: [{
 *         name: "PublicKeyPolicyName",
 *         value: aws_load_balancer_policy["wu-tang-root-ca-pubkey-policy"].policy_name,
 *     }],
 * });
 * const wu_tang_backend_auth_policies_443 = new aws.elb.LoadBalancerBackendServerPolicy("wu-tang-backend-auth-policies-443", {
 *     loadBalancerName: wu_tang.name,
 *     instancePort: 443,
 *     policyNames: [wu_tang_root_ca_backend_auth_policy.policyName],
 * });
 * ```
 *
 * Where the file `pubkey` in the current directory contains only the _public key_ of the certificate.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * ```
 *
 * This example shows how to enable backend authentication for an ELB as well as customize the TLS settings.
 *
 * @deprecated aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy
 */
export class LoadBalancerBackendServerPolicy extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancerBackendServerPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerBackendServerPolicyState, opts?: pulumi.CustomResourceOptions): LoadBalancerBackendServerPolicy {
        pulumi.log.warn("LoadBalancerBackendServerPolicy is deprecated: aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy")
        return new LoadBalancerBackendServerPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:elasticloadbalancing/loadBalancerBackendServerPolicy:LoadBalancerBackendServerPolicy';

    /**
     * Returns true if the given object is an instance of LoadBalancerBackendServerPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancerBackendServerPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancerBackendServerPolicy.__pulumiType;
    }

    /**
     * The instance port to apply the policy to.
     */
    public readonly instancePort!: pulumi.Output<number>;
    /**
     * The load balancer to attach the policy to.
     */
    public readonly loadBalancerName!: pulumi.Output<string>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    public readonly policyNames!: pulumi.Output<string[] | undefined>;

    /**
     * Create a LoadBalancerBackendServerPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy */
    constructor(name: string, args: LoadBalancerBackendServerPolicyArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy */
    constructor(name: string, argsOrState?: LoadBalancerBackendServerPolicyArgs | LoadBalancerBackendServerPolicyState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("LoadBalancerBackendServerPolicy is deprecated: aws.elasticloadbalancing.LoadBalancerBackendServerPolicy has been deprecated in favor of aws.elb.LoadBalancerBackendServerPolicy")
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LoadBalancerBackendServerPolicyState | undefined;
            inputs["instancePort"] = state ? state.instancePort : undefined;
            inputs["loadBalancerName"] = state ? state.loadBalancerName : undefined;
            inputs["policyNames"] = state ? state.policyNames : undefined;
        } else {
            const args = argsOrState as LoadBalancerBackendServerPolicyArgs | undefined;
            if (!args || args.instancePort === undefined) {
                throw new Error("Missing required property 'instancePort'");
            }
            if (!args || args.loadBalancerName === undefined) {
                throw new Error("Missing required property 'loadBalancerName'");
            }
            inputs["instancePort"] = args ? args.instancePort : undefined;
            inputs["loadBalancerName"] = args ? args.loadBalancerName : undefined;
            inputs["policyNames"] = args ? args.policyNames : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(LoadBalancerBackendServerPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancerBackendServerPolicy resources.
 */
export interface LoadBalancerBackendServerPolicyState {
    /**
     * The instance port to apply the policy to.
     */
    readonly instancePort?: pulumi.Input<number>;
    /**
     * The load balancer to attach the policy to.
     */
    readonly loadBalancerName?: pulumi.Input<string>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    readonly policyNames?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a LoadBalancerBackendServerPolicy resource.
 */
export interface LoadBalancerBackendServerPolicyArgs {
    /**
     * The instance port to apply the policy to.
     */
    readonly instancePort: pulumi.Input<number>;
    /**
     * The load balancer to attach the policy to.
     */
    readonly loadBalancerName: pulumi.Input<string>;
    /**
     * List of Policy Names to apply to the backend server.
     */
    readonly policyNames?: pulumi.Input<pulumi.Input<string>[]>;
}
