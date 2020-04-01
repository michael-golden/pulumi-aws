// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a Route53 Hosted Zone.
 * 
 * ## Example Usage
 * 
 * ### Public Zone
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const primary = new aws.route53.Zone("primary", {});
 * ```
 * 
 * ### Public Subdomain Zone
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const main = new aws.route53.Zone("main", {});
 * const dev = new aws.route53.Zone("dev", {
 *     tags: {
 *         Environment: "dev",
 *     },
 * });
 * const devNs = new aws.route53.Record("dev-ns", {
 *     name: "dev.example.com",
 *     records: [
 *         dev.nameServers[0],
 *         dev.nameServers[1],
 *         dev.nameServers[2],
 *         dev.nameServers[3],
 *     ],
 *     ttl: 30,
 *     type: "NS",
 *     zoneId: main.zoneId,
 * });
 * ```
 * 
 * ### Private Zone
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const privateZone = new aws.route53.Zone("private", {
 *     vpcs: [{
 *         vpcId: aws_vpc_example.id,
 *     }],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_zone.html.markdown.
 */
export class Zone extends pulumi.CustomResource {
    /**
     * Get an existing Zone resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState, opts?: pulumi.CustomResourceOptions): Zone {
        return new Zone(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:route53/zone:Zone';

    /**
     * Returns true if the given object is an instance of Zone.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Zone {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Zone.__pulumiType;
    }

    /**
     * A comment for the hosted zone. Defaults to 'Managed by Pulumi'.
     */
    public readonly comment!: pulumi.Output<string>;
    /**
     * The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
     */
    public readonly delegationSetId!: pulumi.Output<string | undefined>;
    /**
     * Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
     */
    public readonly forceDestroy!: pulumi.Output<boolean | undefined>;
    /**
     * This is the name of the hosted zone.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A list of name servers in associated (or default) delegation set.
     * Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
     */
    public /*out*/ readonly nameServers!: pulumi.Output<string[]>;
    /**
     * A mapping of tags to assign to the zone.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegationSetId` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
     */
    public readonly vpcs!: pulumi.Output<outputs.route53.ZoneVpc[] | undefined>;
    /**
     * The Hosted Zone ID. This can be referenced by zone records.
     */
    public /*out*/ readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a Zone resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ZoneArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ZoneArgs | ZoneState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ZoneState | undefined;
            inputs["comment"] = state ? state.comment : undefined;
            inputs["delegationSetId"] = state ? state.delegationSetId : undefined;
            inputs["forceDestroy"] = state ? state.forceDestroy : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nameServers"] = state ? state.nameServers : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcs"] = state ? state.vpcs : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as ZoneArgs | undefined;
            inputs["comment"] = (args ? args.comment : undefined) || "Managed by Pulumi";
            inputs["delegationSetId"] = args ? args.delegationSetId : undefined;
            inputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcs"] = args ? args.vpcs : undefined;
            inputs["nameServers"] = undefined /*out*/;
            inputs["zoneId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Zone.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Zone resources.
 */
export interface ZoneState {
    /**
     * A comment for the hosted zone. Defaults to 'Managed by Pulumi'.
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
     */
    readonly delegationSetId?: pulumi.Input<string>;
    /**
     * Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * This is the name of the hosted zone.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of name servers in associated (or default) delegation set.
     * Find more about delegation sets in [AWS docs](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html).
     */
    readonly nameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the zone.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegationSetId` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
     */
    readonly vpcs?: pulumi.Input<pulumi.Input<inputs.route53.ZoneVpc>[]>;
    /**
     * The Hosted Zone ID. This can be referenced by zone records.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Zone resource.
 */
export interface ZoneArgs {
    /**
     * A comment for the hosted zone. Defaults to 'Managed by Pulumi'.
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * The ID of the reusable delegation set whose NS records you want to assign to the hosted zone. Conflicts with `vpc` as delegation sets can only be used for public zones.
     */
    readonly delegationSetId?: pulumi.Input<string>;
    /**
     * Whether to destroy all records (possibly managed outside of this provider) in the zone when destroying the zone.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * This is the name of the hosted zone.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the zone.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Configuration block(s) specifying VPC(s) to associate with a private hosted zone. Conflicts with the `delegationSetId` argument in this resource and any [`aws.route53.ZoneAssociation` resource](https://www.terraform.io/docs/providers/aws/r/route53_zone_association.html) specifying the same zone ID. Detailed below.
     */
    readonly vpcs?: pulumi.Input<pulumi.Input<inputs.route53.ZoneVpc>[]>;
}
