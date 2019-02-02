// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an Elastic File System (EFS) mount target.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_vpc_foo = new aws.ec2.Vpc("foo", {
 *     cidrBlock: "10.0.0.0/16",
 * });
 * const aws_subnet_alpha = new aws.ec2.Subnet("alpha", {
 *     availabilityZone: "us-west-2a",
 *     cidrBlock: "10.0.1.0/24",
 *     vpcId: aws_vpc_foo.id,
 * });
 * const aws_efs_mount_target_alpha = new aws.efs.MountTarget("alpha", {
 *     fileSystemId: aws_efs_file_system_foo.id,
 *     subnetId: aws_subnet_alpha.id,
 * });
 * ```
 */
export class MountTarget extends pulumi.CustomResource {
    /**
     * Get an existing MountTarget resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MountTargetState, opts?: pulumi.CustomResourceOptions): MountTarget {
        return new MountTarget(name, <any>state, { ...opts, id: id });
    }

    /**
     * The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
     */
    public /*out*/ readonly dnsName: pulumi.Output<string>;
    /**
     * Amazon Resource Name of the file system.
     */
    public /*out*/ readonly fileSystemArn: pulumi.Output<string>;
    /**
     * The ID of the file system for which the mount target is intended.
     */
    public readonly fileSystemId: pulumi.Output<string>;
    /**
     * The address (within the address range of the specified subnet) at
     * which the file system may be mounted via the mount target.
     */
    public readonly ipAddress: pulumi.Output<string>;
    /**
     * The ID of the network interface that Amazon EFS created when it created the mount target.
     */
    public /*out*/ readonly networkInterfaceId: pulumi.Output<string>;
    /**
     * A list of up to 5 VPC security group IDs (that must
     * be for the same VPC as subnet specified) in effect for the mount target.
     */
    public readonly securityGroups: pulumi.Output<string[]>;
    /**
     * The ID of the subnet to add the mount target in.
     */
    public readonly subnetId: pulumi.Output<string>;

    /**
     * Create a MountTarget resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MountTargetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MountTargetArgs | MountTargetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: MountTargetState = argsOrState as MountTargetState | undefined;
            inputs["dnsName"] = state ? state.dnsName : undefined;
            inputs["fileSystemArn"] = state ? state.fileSystemArn : undefined;
            inputs["fileSystemId"] = state ? state.fileSystemId : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["networkInterfaceId"] = state ? state.networkInterfaceId : undefined;
            inputs["securityGroups"] = state ? state.securityGroups : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
        } else {
            const args = argsOrState as MountTargetArgs | undefined;
            if (!args || args.fileSystemId === undefined) {
                throw new Error("Missing required property 'fileSystemId'");
            }
            if (!args || args.subnetId === undefined) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["fileSystemId"] = args ? args.fileSystemId : undefined;
            inputs["ipAddress"] = args ? args.ipAddress : undefined;
            inputs["securityGroups"] = args ? args.securityGroups : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["dnsName"] = undefined /*out*/;
            inputs["fileSystemArn"] = undefined /*out*/;
            inputs["networkInterfaceId"] = undefined /*out*/;
        }
        super("aws:efs/mountTarget:MountTarget", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MountTarget resources.
 */
export interface MountTargetState {
    /**
     * The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
     */
    readonly dnsName?: pulumi.Input<string>;
    /**
     * Amazon Resource Name of the file system.
     */
    readonly fileSystemArn?: pulumi.Input<string>;
    /**
     * The ID of the file system for which the mount target is intended.
     */
    readonly fileSystemId?: pulumi.Input<string>;
    /**
     * The address (within the address range of the specified subnet) at
     * which the file system may be mounted via the mount target.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * The ID of the network interface that Amazon EFS created when it created the mount target.
     */
    readonly networkInterfaceId?: pulumi.Input<string>;
    /**
     * A list of up to 5 VPC security group IDs (that must
     * be for the same VPC as subnet specified) in effect for the mount target.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the subnet to add the mount target in.
     */
    readonly subnetId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MountTarget resource.
 */
export interface MountTargetArgs {
    /**
     * The ID of the file system for which the mount target is intended.
     */
    readonly fileSystemId: pulumi.Input<string>;
    /**
     * The address (within the address range of the specified subnet) at
     * which the file system may be mounted via the mount target.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * A list of up to 5 VPC security group IDs (that must
     * be for the same VPC as subnet specified) in effect for the mount target.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the subnet to add the mount target in.
     */
    readonly subnetId: pulumi.Input<string>;
}
