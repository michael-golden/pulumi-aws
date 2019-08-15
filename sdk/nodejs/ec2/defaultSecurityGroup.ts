// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputApi from "../types/input";
import * as outputApi from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a resource to manage the default AWS Security Group.
 * 
 * For EC2 Classic accounts, each region comes with a Default Security Group.
 * Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
 * destroyed. **This is an advanced resource**, and has special caveats to be aware
 * of when using it. Please read this document in its entirety before using this
 * resource.
 * 
 * The `aws.ec2.DefaultSecurityGroup` behaves differently from normal resources, in that
 * this provider does not _create_ this resource, but instead "adopts" it
 * into management. We can do this because these default security groups cannot be
 * destroyed, and are created with a known set of default ingress/egress rules.
 * 
 * When this provider first adopts the Default Security Group, it **immediately removes all
 * ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
 * configuration. This step is required so that only the rules specified in the
 * configuration are created.
 * 
 * This resource treats its inline rules as absolute; only the rules defined
 * inline are created, and any additions/removals external to this resource will
 * result in diff shown. For these reasons, this resource is incompatible with the
 * `aws.ec2.SecurityGroupRule` resource.
 * 
 * For more information about Default Security Groups, see the AWS Documentation on
 * [Default Security Groups][aws-default-security-groups].
 * 
 * ## Basic Example Usage, with default rules
 * 
 * The following config gives the Default Security Group the same rules that AWS
 * provides by default, but pulls the resource under management by this provider. This means that
 * any ingress or egress rules added or changed will be detected as drift.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const mainvpc = new aws.ec2.Vpc("mainvpc", {
 *     cidrBlock: "10.1.0.0/16",
 * });
 * const defaultDefaultSecurityGroup = new aws.ec2.DefaultSecurityGroup("default", {
 *     egress: [{
 *         cidrBlocks: ["0.0.0.0/0"],
 *         fromPort: 0,
 *         protocol: "-1",
 *         toPort: 0,
 *     }],
 *     ingress: [{
 *         fromPort: 0,
 *         protocol: "-1",
 *         self: true,
 *         toPort: 0,
 *     }],
 *     vpcId: mainvpc.id,
 * });
 * ```
 * 
 * ## Example config to deny all Egress traffic, allowing Ingress
 * 
 * The following denies all Egress traffic by omitting any `egress` rules, while
 * including the default `ingress` rule to allow all traffic.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const mainvpc = new aws.ec2.Vpc("mainvpc", {
 *     cidrBlock: "10.1.0.0/16",
 * });
 * const defaultDefaultSecurityGroup = new aws.ec2.DefaultSecurityGroup("default", {
 *     ingress: [{
 *         fromPort: 0,
 *         protocol: "-1",
 *         self: true,
 *         toPort: 0,
 *     }],
 *     vpcId: mainvpc.id,
 * });
 * ```
 * 
 * ## Usage
 * 
 * With the exceptions mentioned above, `aws.ec2.DefaultSecurityGroup` should
 * identical behavior to `aws.ec2.SecurityGroup`. Please consult [AWS_SECURITY_GROUP](https://www.terraform.io/docs/providers/aws/r/security_group.html)
 * for further usage documentation.
 * 
 * ### Removing `aws.ec2.DefaultSecurityGroup` from your configuration
 * 
 * Each AWS VPC (or region, if using EC2 Classic) comes with a Default Security
 * Group that cannot be deleted. The `aws.ec2.DefaultSecurityGroup` allows you to
 * manage this Security Group, but this provider cannot destroy it. Removing this resource
 * from your configuration will remove it from your statefile and management, but
 * will not destroy the Security Group. All ingress or egress rules will be left as
 * they are at the time of removal. You can resume managing them via the AWS Console.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_security_group.html.markdown.
 */
export class DefaultSecurityGroup extends pulumi.CustomResource {
    /**
     * Get an existing DefaultSecurityGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DefaultSecurityGroupState, opts?: pulumi.CustomResourceOptions): DefaultSecurityGroup {
        return new DefaultSecurityGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/defaultSecurityGroup:DefaultSecurityGroup';

    /**
     * Returns true if the given object is an instance of DefaultSecurityGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DefaultSecurityGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DefaultSecurityGroup.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    public readonly egress!: pulumi.Output<outputApi.ec2.DefaultSecurityGroupEgress[] | undefined>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    public readonly ingress!: pulumi.Output<outputApi.ec2.DefaultSecurityGroupIngress[] | undefined>;
    /**
     * The name of the security group
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The owner ID.
     */
    public /*out*/ readonly ownerId!: pulumi.Output<string>;
    public readonly revokeRulesOnDelete!: pulumi.Output<boolean | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The VPC ID. **Note that changing
     * the `vpcId` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a DefaultSecurityGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DefaultSecurityGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DefaultSecurityGroupArgs | DefaultSecurityGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DefaultSecurityGroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["egress"] = state ? state.egress : undefined;
            inputs["ingress"] = state ? state.ingress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["ownerId"] = state ? state.ownerId : undefined;
            inputs["revokeRulesOnDelete"] = state ? state.revokeRulesOnDelete : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as DefaultSecurityGroupArgs | undefined;
            inputs["egress"] = args ? args.egress : undefined;
            inputs["ingress"] = args ? args.ingress : undefined;
            inputs["revokeRulesOnDelete"] = args ? args.revokeRulesOnDelete : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DefaultSecurityGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DefaultSecurityGroup resources.
 */
export interface DefaultSecurityGroupState {
    readonly arn?: pulumi.Input<string>;
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    readonly egress?: pulumi.Input<pulumi.Input<inputApi.ec2.DefaultSecurityGroupEgress>[]>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    readonly ingress?: pulumi.Input<pulumi.Input<inputApi.ec2.DefaultSecurityGroupIngress>[]>;
    /**
     * The name of the security group
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The owner ID.
     */
    readonly ownerId?: pulumi.Input<string>;
    readonly revokeRulesOnDelete?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The VPC ID. **Note that changing
     * the `vpcId` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DefaultSecurityGroup resource.
 */
export interface DefaultSecurityGroupArgs {
    /**
     * Can be specified multiple times for each
     * egress rule. Each egress block supports fields documented below.
     */
    readonly egress?: pulumi.Input<pulumi.Input<inputApi.ec2.DefaultSecurityGroupEgress>[]>;
    /**
     * Can be specified multiple times for each
     * ingress rule. Each ingress block supports fields documented below.
     */
    readonly ingress?: pulumi.Input<pulumi.Input<inputApi.ec2.DefaultSecurityGroupIngress>[]>;
    readonly revokeRulesOnDelete?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The VPC ID. **Note that changing
     * the `vpcId` will _not_ restore any default security group rules that were
     * modified, added, or removed.** It will be left in its current state
     */
    readonly vpcId?: pulumi.Input<string>;
}
