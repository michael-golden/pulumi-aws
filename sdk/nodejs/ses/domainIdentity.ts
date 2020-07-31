// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an SES domain identity resource
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = new aws.ses.DomainIdentity("example", {domain: "example.com"});
 * const exampleAmazonsesVerificationRecord = new aws.route53.Record("exampleAmazonsesVerificationRecord", {
 *     zoneId: "ABCDEFGHIJ123",
 *     name: "_amazonses.example.com",
 *     type: "TXT",
 *     ttl: "600",
 *     records: [example.verificationToken],
 * });
 * ```
 */
export class DomainIdentity extends pulumi.CustomResource {
    /**
     * Get an existing DomainIdentity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainIdentityState, opts?: pulumi.CustomResourceOptions): DomainIdentity {
        return new DomainIdentity(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ses/domainIdentity:DomainIdentity';

    /**
     * Returns true if the given object is an instance of DomainIdentity.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DomainIdentity {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DomainIdentity.__pulumiType;
    }

    /**
     * The ARN of the domain identity.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The domain name to assign to SES
     */
    public readonly domain!: pulumi.Output<string>;
    /**
     * A code which when added to the domain as a TXT record
     * will signal to SES that the owner of the domain has authorised SES to act on
     * their behalf. The domain identity will be in state "verification pending"
     * until this is done. See below for an example of how this might be achieved
     * when the domain is hosted in Route 53 and managed by this provider.  Find out
     * more about verifying domains in Amazon SES in the [AWS SES
     * docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
     */
    public /*out*/ readonly verificationToken!: pulumi.Output<string>;

    /**
     * Create a DomainIdentity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainIdentityArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DomainIdentityArgs | DomainIdentityState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DomainIdentityState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["domain"] = state ? state.domain : undefined;
            inputs["verificationToken"] = state ? state.verificationToken : undefined;
        } else {
            const args = argsOrState as DomainIdentityArgs | undefined;
            if (!args || args.domain === undefined) {
                throw new Error("Missing required property 'domain'");
            }
            inputs["domain"] = args ? args.domain : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["verificationToken"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DomainIdentity.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DomainIdentity resources.
 */
export interface DomainIdentityState {
    /**
     * The ARN of the domain identity.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The domain name to assign to SES
     */
    readonly domain?: pulumi.Input<string>;
    /**
     * A code which when added to the domain as a TXT record
     * will signal to SES that the owner of the domain has authorised SES to act on
     * their behalf. The domain identity will be in state "verification pending"
     * until this is done. See below for an example of how this might be achieved
     * when the domain is hosted in Route 53 and managed by this provider.  Find out
     * more about verifying domains in Amazon SES in the [AWS SES
     * docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
     */
    readonly verificationToken?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DomainIdentity resource.
 */
export interface DomainIdentityArgs {
    /**
     * The domain name to assign to SES
     */
    readonly domain: pulumi.Input<string>;
}
